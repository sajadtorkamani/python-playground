def esthetic(num: int) -> list[int]:
    result = []

    for base in range(2, 11):
        # Get number in base
        num_in_base = convert_to_base(num, base)

        if is_esthetic(num_in_base):
            result.append(base)

    return result


def is_esthetic(num: int) -> bool:
    nums = [int(char) for char in list(str(num))]

    if len(nums) == 1:
        return True

    for num, current_num in enumerate(nums):
        # Special case: first number
        if num == 0:
            next_num = nums[num + 1]
            if abs(current_num - next_num) != 1:
                return False

        # Special case: last number
        elif num == len(nums) - 1:
            previous_num = nums[num - 1]
            if abs(current_num - previous_num) != 1:
                return False

        # All other numbers
        else:
            next_num = nums[num + 1]
            previous_num = nums[num - 1]

            if abs(current_num - previous_num) != 1 or abs(
                    current_num - next_num) != 1:
                return False

    return True


def convert_to_base(num: int, base: int) -> int:
    if num == 0:
        return 0  # Special case for zero

    result = ""
    while num > 0:
        digit = num % base
        result = str(digit) + result
        num //= base

    return int(result)
