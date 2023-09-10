import math
from functools import reduce


def check_root(string):
    items = string.split(',')

    if len(items) is not 4:
        return 'incorrect input'

    try:
        nums = [int(x) for x in items]
    except ValueError:
        return 'incorrect input'

    for index, num in enumerate(nums[:-1]):
        next_num = nums[index + 1]
        if next_num != (num + 1):
            return 'not consecutive'

    product = reduce(lambda a, b: a * b, nums) + 1
    square = int(math.sqrt(product))

    return f'{product}, {square}'
