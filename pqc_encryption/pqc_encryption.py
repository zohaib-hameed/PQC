import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from cryptography.fernet import Fernet
import oqs
import os 
import sys
import base64
import time
print("Please enter correct path for public and also for file to be encrypted")
PUBLIC_KEY_PATH = input("Enter path to public key:")
if not os.path.exists(PUBLIC_KEY_PATH):
    print(f"\n[!] ERROR THE File '{PUBLIC_KEY_PATH}' not found.stopping.")
    sys.exit()
INPUT_FILE = input("enter path of file to encrypt:")
if not os.path.exists(INPUT_FILE):
    print(f"\n[!] ERROR: The file '{INPUT_FILE}' was not found. so no encryption process takes place")
    sys.exit()
ENCRYPTED_FILE = INPUT_FILE + ".enc"
with open(PUBLIC_KEY_PATH, "rb") as f:
    encoded_public_key = f.read()
public_key_bytes = base64.b64decode(encoded_public_key)
start_time = time.perf_counter()
with oqs.KeyEncapsulation("ML-KEM-512") as client:
    ciphertext, shared_secret = client.encap_secret(public_key_bytes)
end_time = time.perf_counter()
duration_ms = (end_time - start_time) * 1000
with open("kem_ciphertext.bin", "wb") as f:
    f.write(ciphertext)
# Fernet requires a 32-byte URL-safe base64 key
# We take the first 32 bytes of our Kyber secret
aes_key = base64.urlsafe_b64encode(shared_secret)
cipher_suite = Fernet(aes_key)

try:
    with open(INPUT_FILE, "rb") as f:
        original_data = f.read()
    encrypted_data = cipher_suite.encrypt(original_data)

    with open(ENCRYPTED_FILE, "wb") as f:
        f.write(encrypted_data)

    print(f"[SENDER] SUCCESS: File '{INPUT_FILE}' encrypted to '{ENCRYPTED_FILE}'")
    print("-" * 40)
    print(f"PQC Key Encapsulation Time: {duration_ms:.4f} ms")
    print("-" * 40)
except FileNotFoundError:
    print(f"[ERROR] Could not find the file: {INPUT_FILE}")
