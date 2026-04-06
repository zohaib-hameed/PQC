import os, sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
KEY_PATH = input("Enter private key path:")
ENC_PATH = input("Enter file for decryption:")
OUTPUT_FILE = "decrypted_" + ENC_PATH.replace(".encrypted" , "") 
for file in [KEY_PATH, ENC_PATH]:
    if not os.path.exists(file):
        print(f"\n[!] ERROR: '{file}' not found. Check the path and try again.")
        sys.exit()
with open(KEY_PATH, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )
with open(ENC_PATH, "rb") as f:
    iv = f.read(16)                   
    encrypted_aes_key = f.read(256)    
    encrypted_data = f.read()          
aes_key = private_key.decrypt(
    encrypted_aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
cipher = Cipher(algorithms.AES(aes_key), modes.CTR(iv))
decryptor = cipher.decryptor()
plaintext = decryptor.update(encrypted_data) + decryptor.finalize()
with open(OUTPUT_FILE, "wb") as f:
    f.write(plaintext)
print("Decryption successful! File saved as 'document_decrypted.txt'")
