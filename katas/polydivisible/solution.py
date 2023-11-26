def polydivisible(num: int) -> bool:
    nums = [int(digit) for digit in str(num)]

    for index, digit in enumerate(nums):
        iteration = index + 1
        digits = nums[0:iteration]
        digits_num = int(''.join([str(digit) for digit in digits]))

        if digits_num % iteration != 0:
            return False

    return True
