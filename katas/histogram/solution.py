from typing import List
import math


def histogram(rollCounts: List[int]) -> str:
    result = []

    totalRollCount = sum(rollCounts)

    for index, rollCount in enumerate(rollCounts):
        result.append(
            print_line(num=index + 1, numRollCount=rollCount, totalRollCount=totalRollCount)
        )

    result.reverse()

    return str.join("\n", result) + "\n"


def print_line(num: int, numRollCount: int, totalRollCount: int) -> str:
    prefix = f"{num}|"

    if numRollCount == 0:
        return prefix

    percentage = math.floor((numRollCount / totalRollCount) * 100)
    num_bars = math.floor(percentage / 2)
    bars = "█" * num_bars

    return f"{prefix}{bars} {percentage}%"
