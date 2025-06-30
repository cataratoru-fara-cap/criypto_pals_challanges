import base64
from Crypto.Cipher import AES


def ecb_encrypt(plain_text: bytes, key: bytes) -> bytes:
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    return cipher.encrypt(plain_text)


def ecb_decrypt(cipher_text: bytes, key: bytes) -> bytes:
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    return cipher.decrypt(cipher_text)


if __name__ == "__main__":
    file_path = "/home/dragon/Sandbox/criypto_pals_challanges/7_AESsd.txt"
    f = open(file_path).read()
    f = base64.b64decode(f)
    key = b"YELLOW SUBMARINE"
    message = ecb_decrypt(cipher_text=f, key=key)
    print(message.decode())
