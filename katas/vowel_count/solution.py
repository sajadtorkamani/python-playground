import re

def vowel_count(str):
    matches = re.findall("[aeiou]", str)

    return len(matches)

