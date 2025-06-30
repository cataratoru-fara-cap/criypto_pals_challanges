def add_PKCS_padding(plain_text: bytes | bytearray, block_size: int = 16) -> bytearray:
    if isinstance(plain_text, bytes):
        plain_text = bytearray(plain_text)
    elif not isinstance(plain_text, bytearray):
        raise Exception(f"Invalid type {type(plain_text)}")
    n = len(plain_text) % block_size
    for i in range(block_size - n):
        plain_text.append(block_size - n)  # type: ignore

    return plain_text


def remove_PKCS_padding(byte_string: bytes) -> bytes:
    padding_length = byte_string[-1]
    return byte_string[:-padding_length]

if __name__ == "__main__":
    padded = bytearray(b"YELLOW SUBMARINE")
    print(padded)
    print(add_PKCS_padding(padded, 20))
    print(remove_PKCS_padding(b"YELLOW SUBMARINE\x04\x04\x04\x04"))
