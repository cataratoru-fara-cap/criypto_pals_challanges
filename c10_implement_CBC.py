import base64
from email import message
from c7_decrypt_AES import aes_in_ecb
from c3_break_one_byte_xor import XOR_repeating
from c9_PKCS_padding import add_PKCS_padding, remove_PKCS_padding

def cbc_encrypt(key:bytes, IV:bytes, byte_string:bytes) -> bytes:
    output = bytearray()

    byte_string = add_PKCS_padding(byte_string)
    blocks = [byte_string[start:start+16] for start in range(0,len(byte_string), 16)]
    for block in blocks:
        xored = XOR_repeating(input_string=block,key=IV)
        cipher_text = aes_in_ecb(byte_string=xored, key=key, decrypt=False)
        IV = cipher_text
        output  += cipher_text

    return output


def cbc_decrypt(key:bytes, IV:bytes, byte_string:bytes) -> bytes:
    output = bytearray()
    
    blocks = [byte_string[start:start+16] for start in range(0,len(byte_string), 16)]
    prev = IV
    for block in blocks:
        aesd = aes_in_ecb(key=key, byte_string=block, decrypt=True)
        plain_text = XOR_repeating(input_string=aesd, key=prev)
        prev = block
        output += plain_text

    return remove_PKCS_padding(output)

if __name__ == "__main__":
    IV = b'\x00\x00\x00'
    key = b'YELLOW SUBMARINE'
    file_path="/home/dragon/Sandbox/criypto_pals_challanges/10_implement_CBC.txt"
    f = open(file_path,'r').read().strip()
    f = base64.b64decode(f)
    message = cbc_decrypt(key=key, IV=IV, byte_string=f)
    print(message.decode())