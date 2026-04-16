import os
import time
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
start_time = time.perf_counter()
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
end_time = time.perf_counter()
execution_time = (end_time - start_time) * 1000
public_key = private_key.public_key()
with open("private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )
with open("public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )
print(f"Success! RSA keys saved in current directory: {os.getcwd()}")
print(f"Key Generation Speed: {execution_time:.4f} ms")
