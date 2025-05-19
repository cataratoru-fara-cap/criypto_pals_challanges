import base64
from sys import argv
from Crypto.Cipher import AES


def aes_in_ecb(key: bytes, file_path: str, decrypt: bool = True) -> bytes:
    f = open(file_path).read()
    f = base64.b64decode(f)
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    if decrypt:
        return cipher.decrypt(f)
    else:
        return cipher.encrypt(f)


if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"
    message = aes_in_ecb(
        key=key,
        file_path="/home/dragon/Sandbox/criypto_pals_challanges/Set 1/7_AESsd.txt",
    )
    print(message.decode())
