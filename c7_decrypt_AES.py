import base64
from Crypto.Cipher import AES


def ecb_encrypt(plaintext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    return cipher.encrypt(plaintext)


def ecb_decrypt(
    ciphertext: bytes,
    key: bytes,
) -> bytes:
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    return cipher.decrypt(ciphertext)


if __name__ == "__main__":
    file_path = "/home/dragon/Sandbox/criypto_pals_challanges/7_AESsd.txt"
    f = open(file_path).read()
    f = base64.b64decode(f)
    key = b"YELLOW SUBMARINE"
    message = ecb_decrypt(ciphertext=f, key=key)
    print(message.decode())
