def plastic_balance(nums: list[int]) -> list[int]:
    if len(nums) == 1:
        return nums

    remaining_nums = nums.copy()

    while len(remaining_nums) >= 1:
        start_num = remaining_nums.pop(0) if len(remaining_nums) > 0 else 0
        end_num = remaining_nums.pop() if len(remaining_nums) > 0 else 0
        popped_nums_sum = start_num + end_num
        remaining_nums_sum = sum(remaining_nums)

        if popped_nums_sum == remaining_nums_sum:
            return [start_num, *remaining_nums, end_num]

    return []
