# Always operate on raw bytes, never on encoded strs. Only use hex and base64 for pretty-printing.

import sys
import base64


def hex_b64(a):
    hex_str = bytes.fromhex(a)
    base64_str = base64.b64encode(hex_str)
    return base64_str


if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise Exception("Script only accepts one argument")
    elif len(sys.argv) == 2:
        base64_str = hex_b64(sys.argv[1])
        print(base64_str)
