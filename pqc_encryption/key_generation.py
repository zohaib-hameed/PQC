import warnings
import time
warnings.filterwarnings("ignore", category=UserWarning)
import oqs
import base64
start_time = time.perf_counter()
with oqs.KeyEncapsulation("ML-KEM-512") as server:
    public_key = server.generate_keypair()
    private_key = server.export_secret_key()
end_time = time.perf_counter()
time = (end_time - start_time) * 1000
file_path = "public_key.bin"
with open(file_path, "wb") as f:
    f.write(base64.b64encode(public_key))
print(f"Success: Public key generated and saved to public_key.bin")
priv_file_path = "private_key.bin"
with open(priv_file_path, "wb") as f:
    f.write(base64.b64encode(private_key))
print(f"Success: Private key saved to {priv_file_path}")
print("-" * 35)
print(f"PQC (ML-KEM) KEY GEN TIME: {time:.2f} ms")
print("-" * 35)
    
    
