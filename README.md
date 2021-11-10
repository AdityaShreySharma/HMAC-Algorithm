# HMAC-Algorithm
Implementation of HMAC (Hashed Message Authentication Code) Algorithm without importing the in-built Python Library, 'hmac'.

To use a different Hash Algorithm, change the third parameter of the hmacGenerator function from hashlib.sha256 to the preferred choice in the line 136 of the code.

For example - hashlib.sha512, hashlib.sha1 etc.
``` py
# Generating the HMAC Signature
# digest() returns the encoded data in byte format
signature = base64encode(hmacGenerator(key, message, hashlib.sha256).digest())
```

Output with SHA256 as the Hash Algorithm :-
![SHA256](../Digital Assignments\Fall Semester (2021-2022)\ISAA (Project)\Screenshots\SHA256.png)