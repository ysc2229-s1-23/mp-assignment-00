"""
Implements the 'missing number' algorithm as described below:

Given all numbers between 1,2,…,n except one, this function finds the missing number.

Parameters:
n : int
The upper limit of the range from which numbers are given. One number from this range is missing.
Constraints: 2 ≤ n ≤ 2 x 10^5

arr : List[int]
A list of integers representing the given numbers. This list contains n-1 numbers, each number
is distinct and between 1 and n (inclusive).

Returns:
int
The missing number from the range 1 to n.

Example:
missing_number(5, [2, 3, 1, 5])
4

In the given range 1 to 5, the numbers provided are [2, 3, 1, 5]. The missing number is 4.

Note:
This problem can be solved efficiently by using the arithmetic series formula to calculate the
sum of all numbers from 1 to n, then subtracting the sum of the given numbers. The result is
the missing number.
"""
from typing import List

def missing_number(n: int, arr: List[int]) -> int:
    total_sum = (n * (n + 1)) // 2  # total sum of numbers from 1 to n
    given_sum = sum(arr)  # sum of the given numbers

    return total_sum - given_sum
