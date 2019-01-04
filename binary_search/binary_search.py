from typing import List
import math


def binary_search(list: List, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = math.floor((low + high) / 2)  # 向下取整
        guess = list[mid]
        if item == guess:
            return mid
        elif item > guess:
            low = mid + 1
        elif item < guess:
            high = mid - 1
    return None
