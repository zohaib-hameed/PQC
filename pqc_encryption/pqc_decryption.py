import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import oqs
import os
import sys
import base64
import time
from cryptography.fernet import Fernet
print("Make sure to enter absolute path for required files")
PRIVATE_KEY_PATH = input("Please Enter Private Key Path:")
CXT_PATH = input("Please Enter kem ciphertext path:")
ENC_FILE_PATH = input("File To Decrypt:")
DECRYPTED_FILE = "decrypted_" + ENC_FILE_PATH.replace(".enc", "").replace(".encrypted", "") + ".txt"
for file in [PRIVATE_KEY_PATH, CXT_PATH, ENC_FILE_PATH]:
    if not os.path.exists(file):
        print(f"\n[!] ERROR: '{file}' not found. Check the path and try again.")
        sys.exit()
try:
    with open(PRIVATE_KEY_PATH, "rb") as f:
        encoded_priv = f.read()
    secret_key_bytes = base64.b64decode(encoded_priv)
    with open(CXT_PATH, "rb") as f:
        ciphertext = f.read()
    start_time = time.perf_counter()
    with oqs.KeyEncapsulation("ML-KEM-512" , secret_key=secret_key_bytes) as server:
        shared_secret = server.decap_secret(ciphertext)
    end_time = time.perf_counter()
    decap_time_ms = (end_time - start_time) * 1000
    print("[RECIPIENT] Shared Secret recovered successfully.")
    aes_key = base64.urlsafe_b64encode(shared_secret)
    cipher_suite = Fernet(aes_key)
    with open(ENC_FILE_PATH, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(DECRYPTED_FILE, "wb") as f:
        f.write(decrypted_data)
    print(f"[RECIPIENT] SUCCESS: File decrypted to {DECRYPTED_FILE}")
    print(f"Original Content: {decrypted_data.decode('utf-8')}")
    print("-" * 40)
    print(f"PQC Key Decapsulation Time: {decap_time_ms:.4f} ms")
    print("-" * 40)
except Exception as e:
    print(f"[ERROR] Decryption failed: {e}")
