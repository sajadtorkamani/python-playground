def magic_sum(nums):
    if nums is None:
        return False

    return sum(num for num in nums if num % 2 == 1 and '3' in str(num))
