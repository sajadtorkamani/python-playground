import re


def nothing_special(s):
    return re.sub('[^A-Za-z0-9\s]', '', s) if isinstance(s, str) else 'Not a string!'

