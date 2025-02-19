def hex_to_string(hex_str):
    """Convert a hex string to a decoded string."""
    hex_bytes = bytes.fromhex(hex_str)
    decoded_string = hex_bytes.decode('utf-8')
    return decoded_string


def char_to_dec(string):
    """Convert each character in a string to its decimal (ASCII) value."""
    return [ord(char) for char in string]


def split_table(table, chunk_size=5):
    """Split a table into mini arrays of a specified size."""
    return [table[i:i + chunk_size] for i in range(0, len(table), chunk_size)]


def get_key(chunks, start_flag="THM{", end_flag="}"):
    """Generate the secret key based on the first and last chunks."""
    secret = []
    # Get the first part of the key from the start flag
    for i in range(len(start_flag)):
        secret.append(chr(chunks[0][i] ^ ord(start_flag[i])))
    # Get the last part of the key from the end flag
    secret.append(chr(ord(end_flag) ^ chunks[-1][-1]))
    return secret


def get_flag(chunks, secret):
    """Reconstruct the flag using the secret key."""
    return ''.join([chr(chunk[i] ^ ord(secret[i])) for chunk in chunks for i in range(len(chunk))])


if __name__ == "__main__":
    hex_str = "22033a0b36472a1b1e323333033132027f141b2537250543271a070e1813043f0e4033043338023b"

    # Convert hex to string
    decoded_string = hex_to_string(hex_str)
    print("Decoded String:", decoded_string)

    # Convert string to decimal list
    decimal_list = char_to_dec(decoded_string)
    print("Decimal List:", decimal_list)

    # Split the table into chunks
    chunks = split_table(decimal_list)
    print("Chunks:", chunks)

    # Get the secret key
    key = get_key(chunks)
    print("Secret Key:", ''.join(key))

    # Reconstruct the flag
    flag = get_flag(chunks, key)
    print("Flag:", flag)