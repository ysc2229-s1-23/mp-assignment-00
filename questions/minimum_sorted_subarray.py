"""
Find the length of the smallest subarray that, when sorted, will sort the entire array.

This function takes an array of integers and returns the length of the minimal contiguous subarray
that needs to be sorted in ascending order for the whole array to be sorted.

Parameters:
    arr (List[int]): The input array of integers.

Returns:
    int: The length of the smallest subarray that needs to be sorted. Returns 0 if the array is already sorted.

Example:
    >>> length_smallest_subarray([1, 2, 5, 3, 7, 10, 9, 12])
    5
    >>> length_smallest_subarray([1, 3, 2, 0, -1, 7, 10])
    5
    >>> length_smallest_subarray([1, 2, 3])
    0
    >>> length_smallest_subarray([3, 2, 1])
    3
"""
from typing import List

def length_smallest_subarray(arr: List[int]) -> int:
    pass
