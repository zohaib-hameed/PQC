import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import os
import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
input_file_path = input("Please enter file path to encrypt:")
public_key_path = input("please enter path of public key:")
# Check if all required files exist
for file in [input_file_path, public_key_path]:
    if not os.path.exists(file):
        print(f"\n[!] ERROR: '{file}' not found. Check the path and try again.")
        sys.exit()
with open(public_key_path, "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())
aes_key = os.urandom(32)  
iv = os.urandom(16)
with open(input_file_path, "rb") as f:
    plaintext = f.read()
cipher = Cipher(algorithms.AES(aes_key), modes.CTR(iv))
encryptor = cipher.encryptor()
encrypted_data = encryptor.update(plaintext) + encryptor.finalize()
encrypted_aes_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
output_name = input_file_path + ".encrypted"
with open(output_name, "wb") as f:
    f.write(iv)                # 16 bytes
    f.write(encrypted_aes_key) # 256 bytes (for RSA 2048)
    f.write(encrypted_data)    # Remainder of the file
print(f"Encryption complete. file saved as '{output_name}'")




