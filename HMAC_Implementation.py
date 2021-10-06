import hashlib
import binascii

def b64encode(s, altchars=None):
    encoded = binascii.b2a_base64(s, newline=False)
    if altchars is not None:
        assert len(altchars) == 2, repr(altchars)
        return encoded.translate(bytes.maketrans(b'+/', altchars))
    return encoded

import hashlib as _hashlib

trans_5C = bytes((x ^ 0x5C) for x in range(256))
trans_36 = bytes((x ^ 0x36) for x in range(256))
digest_size = None

class HMAC:
    blocksize = 64 
    def __init__(self, key, msg=None, digestmod=''):
        if callable(digestmod):
            self._digest_cons = digestmod
        elif isinstance(digestmod, str):
            self._digest_cons = lambda d=b'': _hashlib.new(digestmod, d)
        else:
            self._digest_cons = lambda d=b'': digestmod.new(d)

        self._outer = self._digest_cons()
        self._inner = self._digest_cons()
        self.digest_size = self._inner.digest_size

        if hasattr(self._inner, 'block_size'):
            blocksize = self._inner.block_size
            if blocksize < 16:
                blocksize = self.blocksize
        else:
            blocksize = self.blocksize
        self.block_size = blocksize

        if len(key) > blocksize:
            key = self._digest_cons(key).digest()

        key = key.ljust(blocksize, b'\0')
        self._outer.update(key.translate(trans_5C))
        self._inner.update(key.translate(trans_36))
        if msg is not None:
            self.update(msg)

    @property
    def outer(self):
        return self._outer

    def update(self, msg):
        self._inner.update(msg)

    def _current(self):
        h = self._outer.copy()
        h.update(self._inner.digest())
        return h

    def digest(self):
        h = self._current()
        return h.digest()

def new(key, msg=None, digestmod=''):
    return HMAC(key, msg, digestmod)

message = bytes('Message', 'utf-8')
secret = bytes('secret', 'utf-8')
signature = b64encode(new(secret, message, hashlib.sha256).digest())
print(signature)

