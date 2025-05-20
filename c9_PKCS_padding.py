def add_PKCS_padding(plaintext: bytes | bytearray, block_size: int = 16) -> bytearray:
    if isinstance(plaintext, bytes):
        plaintext = bytearray(plaintext)
    elif not isinstance(plaintext, bytearray):
        raise Exception(f"Invalid type {type(plaintext)}")
    n = len(plaintext) % block_size
    for i in range(block_size - n):
        plaintext.append(block_size - n)  # type: ignore

    return plaintext


def remove_PKCS_padding(byte_string: bytes) -> bytes:
    padding_length = byte_string[-1]
    return byte_string[:-padding_length]


if __name__ == "__main__":
    padded = bytearray(b"YELLOW SUBMARINE")
    print(padded)
    print(add_PKCS_padding(padded, 20))
    print(remove_PKCS_padding(b"YELLOW SUBMARINE\x04\x04\x04\x04"))
