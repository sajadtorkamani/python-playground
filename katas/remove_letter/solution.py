def remove_letter(string, n):
    result = string
    letters_to_remove = sorted(string)[:n]

    for letter in letters_to_remove:
        result = result.replace(letter, '', 1)

    return result
