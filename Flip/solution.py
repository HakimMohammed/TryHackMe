'''
access_username= | admin&password=s | Up3rPaSs1

Providing the username admin and password sUp3rPaSs1 will not work
as the server checks if the message contains admin&password=sUp3rPaSs1.

So Lets try to provide 'xdmin' as the username and use
Bit Flip Attack to convert it to 'admin' and get the flag.
'''

from binascii import unhexlify, hexlify

def flip_bits(cipher_text):
    # We need to turn 'x' to 'a'
    xor_diff = ord('x') ^ ord('a')

    cipher_bytes = unhexlify(cipher_text)
    first_byte = cipher_bytes[:1]
    first_byte = bytes([first_byte[0] ^ xor_diff])
    cipher_bytes = first_byte + cipher_bytes[1:]
    print(hexlify(cipher_bytes).decode())

if __name__ == '__main__' :
    cipher_text = "023b8a36f0e567065f2e8c85ba2444e0528fcd056f53fc869fa2d270702c93a2f8257f41765a4a0baaaef801a6e12956"
    flip_bits(cipher_text)