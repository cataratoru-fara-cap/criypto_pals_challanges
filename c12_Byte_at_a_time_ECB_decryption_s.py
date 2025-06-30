import base64
from c7_decrypt_AES import ecb_encrypt
from c9_PKCS_padding import add_PKCS_padding
from c11_ECB_CBC_oracle import generate_random_bytes, generate_random_size

global_key = generate_random_bytes(16)
postfix_string = bytearray(base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"))

def ecb_init_oracle(plain_text: bytearray, random_key: bytes) -> bytes:
    if not isinstance(plain_text, bytearray) or not isinstance(random_key, bytes):
        raise Exception(f"Invalid input type {type(plain_text)}, {type(random_key)}")

    working_copy = bytearray(plain_text)
    working_copy += postfix_string
    working_copy = add_PKCS_padding(plain_text=working_copy)

    # added print stmnts for verification
    return ecb_encrypt(plain_text=working_copy, key=random_key)

if __name__ == "__main__":
    plain_text = bytearray(b"A")
    untapped_text = ecb_init_oracle(bytearray(), random_key=global_key)
    cipher_text = ecb_init_oracle(plain_text=plain_text, random_key=global_key)

    while(len(untapped_text) == len(cipher_text)):
        # Incrementally increase the input size to detect the block length
        plain_text += b"A"
        cipher_text = ecb_init_oracle(plain_text=plain_text, random_key=global_key)

    block_length = len(cipher_text) - len(untapped_text)
    print(f"Detected block length: {block_length}")