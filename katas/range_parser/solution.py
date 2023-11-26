import re


def range_parser(num_ranges: str) -> list[int]:
    result = []

    num_ranges = num_ranges.replace(' ', '').split(',')

    for num_range in num_ranges:
        # Handle range between two numbers
        if '-' in num_range:
            # Assume default step is 1
            if ':' not in num_range:
                num_range += ':1'

            step = int(num_range.split(':')[1])
            num_range = re.sub(':.+', '', num_range)
            start, end = [int(num) for num in num_range.split('-')]
            result += list(range(start, end + 1, step))

        # Handle single number
        else:
            result.append(int(num_range))

    return result
