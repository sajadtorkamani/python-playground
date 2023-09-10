def find_all(haystack, needle):
    indices = []

    for index, item in enumerate(haystack):
        if item == needle:
            indices.append(index)

    return indices

