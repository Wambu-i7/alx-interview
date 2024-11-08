#!/usr/bin/python3
""" This script defines a function `validUTF8` to check if a list of integers represents valid UTF-8 encoded characters."""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    :param data: List[int] - List of integers representing bytes.
    :return: bool - True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes remaining to be validated as continuation bytes
    num_bytes = 0

    # Masks for checking byte patterns
    mask1 = 1 << 7      # 10000000 in binary
    mask2 = 1 << 6      # 01000000 in binary

    for byte in data:
        # Get only the 8 least significant bits of the integer (1 byte)
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in the character
            if (byte & mask1) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                # Invalid case (bytes cannot start with 11111xxx)
                return False
            elif (byte & (mask1 >> 3)) == (mask1 >> 3):
                # 4-byte character (11110xxx)
                num_bytes = 3
            elif (byte & (mask1 >> 2)) == (mask1 >> 2):
                # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte & (mask1 >> 1)) == (mask1 >> 1):
                # 2-byte character (110xxxxx)
                num_bytes = 1
            else:
                # Invalid leading byte
                return False
        else:
            # Check if this byte is a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
