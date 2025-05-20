h1 = b"this is a test"
h2 = b"wokka wokka!!!"
import base64

from itertools import combinations
from numpy import average

from c3_break_one_byte_xor import bxor, break_one_byte_xor


def hamming_distance(h1: bytes | str, h2: bytes | str) -> int:
    if isinstance(h1, str):
        h1 = bytes.fromhex(h1)
    if isinstance(h2, str):
        h2 = bytes.fromhex(h2)

    distance = 0
    for b1, b2 in zip(h1, h2):
        distance += bin(b1 ^ b2).count("1")

    return distance


# array code in order to check recurance, if we have multiple key candidates and the text is long enough
# the minimum value will repeat every keylength times for the encription key used
def find_key_size(cipher_text: str | bytes, max_key_size: int = 40) -> tuple | list:
    min_score = 8.0  # 8 is the maximum hamming-distance between any 2 bytes
    key_length = len(cipher_text)
    # key_sizes : list[tuple] = []
    if isinstance(cipher_text, str):
        cipher_text = base64.b64decode(cipher_text)
    for keysize in range(2, max_key_size):
        chunks = [
            cipher_text[start : start + keysize]
            for start in range(0, len(cipher_text), keysize)
        ]
        subgroup = chunks[:4]

        avg_per_byte = (
            average([hamming_distance(a, b) for a, b in combinations(subgroup, 2)])
            / keysize
        )
        if avg_per_byte < min_score:
            min_score = avg_per_byte
            key_length = keysize
        # key_sizes.append((avg_per_byte, keysize))

    return (key_length, min_score)  # sorted(key_sizes)


def break_repeating_xor(cipher_text: str | bytes) -> bytes:
    keysize = find_key_size(cipher_text)[0]
    if isinstance(cipher_text, str):
        cipher_text = base64.b64decode(cipher_text)
    chunks = [
        cipher_text[start : start + keysize]
        for start in range(0, len(cipher_text), keysize)
    ]
    # Transpose the chunks: group all bytes at the same position in each chunk
    transposed = [
        bytes(chunk[i] for chunk in chunks if len(chunk) > i) for i in range(keysize)  # type: ignore
    ]
    key = bytearray()
    for piece in transposed:
        key += break_one_byte_xor(piece, True)

    return key


if __name__ == "__main__":
    cipher_text = (
        open("/home/dragon/Sandbox/criypto_pals_challanges/6_xored.txt").read().strip()
    )
    cipher_text = bytearray(base64.b64decode(cipher_text))
    key = break_repeating_xor(cipher_text)
    print(key.decode())

    plain_txt = bxor(cipher_text, key)
    print(plain_txt.decode())
