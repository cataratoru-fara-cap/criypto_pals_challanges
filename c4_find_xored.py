from c3_break_one_byte_xor import bxor, break_one_byte_xor, calculate_score

f = open("/home/dragon/Sandbox/criypto_pals_challanges/4_xored.txt").read().split("\n")

max_score = 0
key = bytes()
decrypted_text = bytes()

for i, line in enumerate(f):
    possible_key = break_one_byte_xor(line)
    possible_decrypted_text = bxor(line, possible_key)
    current = calculate_score(bxor(line, possible_key))

    if current > max_score:
        max_score = current
        key = possible_key
        decrypted_text = possible_decrypted_text

print(
    f"Key: {key.decode()}, Decrypted Text: {decrypted_text.decode().strip()}, Score: {max_score:.2f}"
)
# for key, value in valid_decrypts.items():
#     if value[1] > 125:
