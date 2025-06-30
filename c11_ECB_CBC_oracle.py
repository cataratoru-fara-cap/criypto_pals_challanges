import secrets

from c7_decrypt_AES import ecb_encrypt, ecb_decrypt
from c9_PKCS_padding import add_PKCS_padding
from c10_implement_CBC import cbc_encrypt, cbc_decrypt


def generate_random_bytes(size: int = 5) -> bytes:
    return secrets.token_bytes(size)


def generate_random_size(lower_bound: int = 5, upper_bound: int = 11) -> int:
    return lower_bound + secrets.randbelow(upper_bound - lower_bound)


def ecb_cbc_init_oracle(plain_text: bytearray) -> bytes:
    if not isinstance(plain_text, bytearray):
        raise Exception(f"Invalid input type {type(plain_text)}")

    key = generate_random_bytes(16)
    p_size, s_size = generate_random_size(), generate_random_size()
    prefix, suffix = generate_random_bytes(p_size), generate_random_bytes(s_size)
    plain_text = bytearray(prefix) + plain_text + bytearray(suffix)
    plain_text = add_PKCS_padding(plain_text=plain_text)
    seed = secrets.randbelow(2)

    # added print stmnts for verification
    if seed == 0:
        print("encripted with ecb")
        return ecb_encrypt(plain_text=plain_text, key=key)
    print("encrypted with cbc")
    return cbc_encrypt(plain_text=plain_text, key=key, IV=generate_random_bytes(16))


def ecb_cbc_determination_oracle(ciphertext: bytes) -> str:
    blocks = [ciphertext[start : start + 16] for start in range(0, len(ciphertext), 16)]

    if len(set(blocks)) == len(blocks):
        return "CBC"
    else:
        return "ECB"


if __name__ == "__main__":
    plain_text = bytearray(48)
    ciphertext = ecb_cbc_init_oracle(plain_text=plain_text)
    mode = ecb_cbc_determination_oracle(ciphertext=ciphertext)
    print(mode)
