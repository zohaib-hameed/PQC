# 🔐 Multi-Era Cryptography Suite  
### Hybrid Classical (RSA + AES) & Post-Quantum (ML-KEM) Security

This project demonstrates a dual-layered approach to data security, combining industry-standard classical encryption with cutting-edge quantum-resistant algorithms.

It is designed to showcase secure software development practices, including dynamic input validation and hybrid cryptographic architectures.

---

## 📁 Project Structure


/classical_encryption
├── key_generation.py
├── encryption.py
└── decryption.py

/pqc_encryption
├── key_generation.py
├── key_encapsulation.py
└── key_decryption.py


- **/classical_encryption**  
  Implements a hybrid **RSA-2048 + AES-256 (CTR mode)** encryption system.

- **/pqc_encryption**  
  Implements a **Post-Quantum Key Encapsulation Mechanism (KEM)** using  
  **ML-KEM-512 (Kyber)** — a NIST-standardized algorithm.

---

## 🛡️ Features

- ✅ **Adaptive Input**  
  Prompts users for file paths and keys at runtime (no hardcoded paths).

- ✅ **Robust Validation**  
  Uses `os.path.exists` checks to prevent runtime errors and ensure file availability.

- ✅ **Hybrid Architecture**  
  Combines:
  - Asymmetric encryption (**RSA / ML-KEM**) for secure key exchange  
  - Symmetric encryption (**AES / Fernet**) for fast data processing

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python **3.10+**

- Install required cryptography library:
```bash
pip install cryptography



▶️ How to Use

1️⃣ Classical Encryption

1. Generate keys:

 python key_generation.py


2. Encrypt a file:

python encryption.py

3. Decrypt the file:

python decryption.py


2️⃣ Post-Quantum Encryption

1. Generate quantum-safe keys:

 python key_generation.py


2. Encapsulate and encrypt:
 
 python key_encapsulation.py


3. Decapsulate and decrypt:

 python key_decryption.py


