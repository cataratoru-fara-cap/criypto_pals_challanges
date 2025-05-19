def add_PKCS_padding(plaintext: bytes | bytearray, block_size: int = 16) -> bytes:
    if isinstance(plaintext, bytes):
        plaintext = bytearray(plaintext)
    n = len(plaintext) % block_size
    for i in range(block_size - n):
        plaintext.append(block_size - n)  # type: ignore

    return plaintext


if __name__ == "__main__":
    padded = bytearray(b"YELLOW SUBMARINE")
    print(padded)
    print(add_PKCS_padding(padded, 20))
