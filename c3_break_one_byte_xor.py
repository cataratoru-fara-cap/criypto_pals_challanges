letterScores = [
    8.167,
    1.492,
    2.782,
    4.253,
    12.702,
    2.228,
    2.015,
    6.094,
    6.966,
    0.153,
    0.772,
    4.025,
    2.406,
    6.749,
    7.507,
    1.929,
    0.095,
    5.987,
    6.327,
    9.056,
    2.758,
    0.978,
    2.360,
    0.150,
    1.974,
    0.074,
]


def bxor(input_string: str | bytes, key: str | bytes) -> bytes:
    xord_output = bytearray()
    if isinstance(input_string, str):
        input_string = bytes.fromhex(input_string)
    if isinstance(key, str):
        key = bytes.fromhex(key)

    for i in range(len(input_string)):
        xord_output.append(input_string[i] ^ key[i % len(key)])  # type: ignore
    return bytes(xord_output)


def calculate_score(string: bytes) -> float:
    string = string.lower()
    score = 0
    for char in string:
        if char in bytes(b"abcdefghijklmnopqrstuvxywz") and ord("a") <= char <= ord("z"):  # type: ignore
            score += letterScores[char - ord("a")]
        elif char == ord(" "):
            score += 15
    return score


def break_one_byte_xor(ciphertext: str | bytes, assume_just_alphabet: bool = False) -> bytes:  # type: ignore
    max_score: float = 0
    key: bytes = b""

    if isinstance(ciphertext, str):
        ciphertext = bytes.fromhex(ciphertext)

    possible_keys = bytes(range(256))
    for possible_key in possible_keys:
        possible_key_bytes = bytes([possible_key])
        decrypted_txt = bxor(ciphertext, possible_key_bytes)
        if (
            assume_just_alphabet
            and all((32 <= b < 127) or b in (9, 10, 13) for b in decrypted_txt)
            and max_score < calculate_score(decrypted_txt)
        ):
            max_score = calculate_score(decrypted_txt)
            key = possible_key_bytes
        elif not assume_just_alphabet and max_score < calculate_score(decrypted_txt):
            max_score = calculate_score(decrypted_txt)
            key = possible_key_bytes

    return key


# Print the decrypted texts and their keys
if __name__ == "__main__":
    key = break_one_byte_xor(
        "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", True
    )
    print(
        bxor(
            "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736",
            key=key,
        )
    )
