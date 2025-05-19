from binascii import unhexlify

def detect_AES(path_to_file: str, block_size: int = 16) -> list[bytes]:
    message = []
    file = open(path_to_file).read().split("\n")
    file = [unhexlify(line) for line in file]

    for line in file:
        if len(line) % block_size != 0:
            raise Exception("ciphertext length is not multiple of blocksize")

        blocks = [
            line[start : start + block_size]
            for start in range(0, len(line), block_size)
        ]
        if len(set(blocks)) != len(blocks):
            message.append(line)

    return message


if __name__ == "__main__":
    message = detect_AES(
        path_to_file="/home/dragon/Sandbox/criypto_pals_challanges/Set 1/8_detect_AES.txt"
    )

    print(message)
