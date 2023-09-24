def best_friend(text: str, a: str, b: str):
    if text[-1] == a:
        return False

    for index, current_char in enumerate(list(text)):
        # Skip chars that aren't "a"
        if current_char is not a:
            continue

        next_char = text[index + 1]

        if next_char is not b:
            return False

    return True
