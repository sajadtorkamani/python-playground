def duplicate_elements(list_a, list_b):
    for item in list_a:
        if item in list_b:
            return True

    return False
