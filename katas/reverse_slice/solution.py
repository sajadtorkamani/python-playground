def reverse_slice(str):
    str_len = len(str)
    reversed_str = str[::-1]

    return [reversed_str[index:str_len] for index, val in enumerate(reversed_str)]
