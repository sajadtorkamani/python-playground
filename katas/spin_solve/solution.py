import re

"""
- Split sentence into array of words.
- Iterate over each word and apply transformation if needed:
    --
    Condition: Word is longer than 6 chars or has 2 or more 'T' or 't' in it.
    Action: Convert it backwards
    ---
    Condition: Word is exactly 2 chars long or before a comma
    Action: Convert to uppercase
    ---
    Condition: Condition: Word is exactly 1 char long or before a comma
    Action: Convert to 0
"""


def spin_solve(sentence: str) -> str:
    words = sentence.split()
    result = []

    for word in words:
        length = len(get_non_punctuation_letters(word))

        if length > 6 or len(re.findall("[tT]", word)) >= 2:
            result.append(reverse(word))

        elif length == 2 or word[-1] == ",":
            result.append(word.upper())

        elif length == 1:
            result.append("0")

        else:
            result.append(word)

    return str.join(" ", result)


def reverse(word: str) -> str:
    return get_non_punctuation_letters(word)[::-1] + get_punctuation_letters(word)


def get_non_punctuation_letters(word: str) -> str:
    letters = re.search("[^.,]+", word)

    if letters:
        return letters.group(0)
    else:
        return ""


def get_punctuation_letters(word: str) -> str:
    punctuation = re.search("[.,]+", word)

    if punctuation:
        return punctuation.group(0)
    else:
        return ""
