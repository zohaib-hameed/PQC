import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import oqs
import base64 
with oqs.KeyEncapsulation("ML-KEM-512") as server:
    public_key = server.generate_keypair()
    private_key = server.export_secret_key()
file_path = "public_key_pqc.bin"
with open(file_path, "wb") as f:
    f.write(base64.b64encode(public_key))
print(f"Success: Public key generated and saved to public_key_pqc.bin")
priv_file_path = "private_key_pqc.bin"
with open(priv_file_path, "wb") as f:
    f.write(base64.b64encode(private_key))
print(f"Success: Private key saved to {priv_file_path}")

    
    
