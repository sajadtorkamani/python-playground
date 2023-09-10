# Excuse the mess, I'm learning Python
def rev_sub(arr: list) -> list:
    even_lists = get_even_lists(arr)
    indices = list(even_lists.keys())
    reversed_list = []
    indices_changed = []

    for index, num in enumerate(arr):
        if index in indices:
            sub_list = even_lists[index]
            reversed_sub_list = sub_list[::-1]

            reversed_list = reversed_list + reversed_sub_list

            for sub_list_index in range(len(sub_list)):
                indices_changed.append(index + sub_list_index)
        else:
            if index not in indices_changed:
                reversed_list.append(num)

    return reversed_list


def get_even_lists(arr: list) -> dict:
    even_lists = {}

    for index, num in enumerate(arr):
        prev_num = arr[index - 1] if index > 0 else None

        is_start_of_list = is_even(num) and not is_even(prev_num)
        is_part_of_list = is_even(num) and is_even(prev_num)

        indices = list(even_lists.keys())
        last_index = indices[-1] if len(indices) > 0 else None

        if is_start_of_list:
            even_lists[index] = [num]
        elif is_part_of_list:
            even_lists[last_index].append(num)

    return even_lists


def get_indices_to_change(arr: list) -> list:
    indices = []
    even_lists = get_even_lists(arr)

    for key in even_lists:
        print(key)

    return indices


def is_even(num: int = None) -> bool:
    if num is None:
        return False

    return num % 2 == 0
