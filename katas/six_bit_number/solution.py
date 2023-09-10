import re


def six_bit_number(s):
    if re.match(r'^[1-9]?\d\Z$', s) is None:
        return False

    num = int(s)

    return num >= 0 and num <= 63
