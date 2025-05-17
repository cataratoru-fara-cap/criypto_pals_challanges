import base64
from sys import argv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def decrypt_aes_128_ecb(key: bytes, file_path: str) -> bytes:
    cipher = Cipher(algorithm=algorithms.AES128(key=key), mode=modes.ECB())
    f = open(file_path).read()
    f = base64.b64decode(f)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(f) + decryptor.finalize()
    message = decrypted_data
    return message


if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"
    message = decrypt_aes_128_ecb(
        key=key,
        file_path="/home/dragon/Sandbox/criypto_pals_challanges/Set 1/7_AESsd.txt",
    )
    print(message.decode())
