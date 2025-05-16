from s3_break_one_byte_xor import XOR_repeating

print(
    XOR_repeating(
        b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal",
        b"ICE",
    ).hex()
)
