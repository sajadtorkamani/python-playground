def get_strings(city):
    char_dict = {}
    chars = city.lower().replace(' ', '')

    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return ','.join([f"{char}:{'*' * char_count}" for char, char_count in char_dict.items()])
