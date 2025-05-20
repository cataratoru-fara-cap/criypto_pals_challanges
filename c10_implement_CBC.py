import base64
from email import message
from c7_decrypt_AES import ecb_decrypt, ecb_encrypt
from c3_break_one_byte_xor import bxor
from c9_PKCS_padding import add_PKCS_padding, remove_PKCS_padding


def cbc_encrypt(plaintext: bytes, key: bytes, IV: bytes) -> bytes:
    output = bytes()

    plaintext = add_PKCS_padding(plaintext)
    blocks = [plaintext[start : start + 16] for start in range(0, len(plaintext), 16)]
    for block in blocks:
        xored = bxor(input_string=block, key=IV)
        cipher_text = ecb_encrypt(plaintext=xored, key=key)
        IV = cipher_text
        output += cipher_text

    return output


def cbc_decrypt(ciphertext: bytes, key: bytes, IV: bytes) -> bytes:  # type: ignore
    output = bytes()

    blocks = [ciphertext[start : start + 16] for start in range(0, len(ciphertext), 16)]
    prev = IV
    for block in blocks:
        toxor = ecb_decrypt(ciphertext=block, key=key)
        plain_text = bxor(input_string=toxor, key=prev)
        prev = block
        output += plain_text

    return remove_PKCS_padding(output)


if __name__ == "__main__":
    IV = b"\x00\x00\x00"
    key = b"YELLOW SUBMARINE"
    file_path = "/home/dragon/Sandbox/criypto_pals_challanges/10_implement_CBC.txt"
    f = open(file_path, "r").read().strip()
    f = base64.b64decode(f)
    message = cbc_decrypt(key=key, IV=IV, ciphertext=f)
    print(message.decode())
