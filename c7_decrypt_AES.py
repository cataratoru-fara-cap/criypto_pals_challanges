import base64
from sys import argv
from Crypto.Cipher import AES


def aes_in_ecb(key: bytes, byte_string: bytes, decrypt: bool = True) -> bytes:
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    if decrypt:
        return cipher.decrypt(byte_string)
    else:
        return cipher.encrypt(byte_string)


if __name__ == "__main__":
    file_path = "/home/dragon/Sandbox/criypto_pals_challanges/7_AESsd.txt"
    f = open(file_path).read()
    f = base64.b64decode(f)
    key = b"YELLOW SUBMARINE"
    message = aes_in_ecb(key=key, byte_string=f)
    print(message.decode())
