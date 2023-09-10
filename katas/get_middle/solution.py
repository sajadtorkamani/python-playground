def get_middle(str):
    length = len(str)
    mid_index = length // 2

    if length % 2 == 0:
        return str[mid_index - 1] + str[mid_index]
    else:
        return str[mid_index]
