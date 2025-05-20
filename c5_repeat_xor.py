from c3_break_one_byte_xor import bxor

print(
    bxor(
        b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal",
        b"ICE",
    ).hex()
)
