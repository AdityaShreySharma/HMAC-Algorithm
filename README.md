# HMAC-Algorithm
Implementation of HMAC (Hashed Message Authentication Code) Algorithm without importing the in-built Python Library, 'hmac'.

To use a different Hash Algorithm, change the third parameter of the hmacGenerator function from hashlib.sha256 to the preferred choice in the line 136 of the code.

For example - hashlib.sha512, hashlib.sha1 etc.
``` py
# Generating the HMAC Signature
# digest() returns the encoded data in byte format
signature = base64encode(hmacGenerator(key, message, hashlib.sha256).digest())
```

Output with SHA-256 as the Hash Algorithm :-

![SHA256](https://user-images.githubusercontent.com/65895246/141085311-a6cfda87-b773-418b-a37f-1325789309a4.PNG)

Output with SHA-512 as the Hash Algorithm :-

![SHA512](https://user-images.githubusercontent.com/65895246/141085397-23ae0b97-1bd8-4093-aee9-2883487e63f2.PNG)
