from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """
    Given a sorted array of distinct integers and a target value,
    return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    """

    # binary search
    left, right = 0, len(nums) - 1  # inclusive indexes of part of the list we care about
    while left <= right:  # = helps make sure that we get correct index when adding to the right most index
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle  # if element in the list
        elif target > nums[middle]:
            left = middle + 1
        elif target < nums[middle]:
            right = middle - 1
    return left  # if element not in the list


n = [1, 2, 3, 4, 5, 6, 7, 8]
t = 5
print(search_insert(n, t))
