import sys


def xor(str1: str, str2: str):
    bytes1 = bytes.fromhex(str1)
    bytes2 = bytes.fromhex(str2)

    return bytearray([bit1 ^ bit2 for bit1, bit2, in zip(bytes1, bytes2)])


if __name__ == "__main__" and len(sys.argv) == 3:
    print(xor(sys.argv[1], sys.argv[2]))
else:
    raise Exception("Usage: <str1> xor <str2>")
