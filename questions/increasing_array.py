"""
Given an array of n integers, this function modifies the array so that it is 
increasing, i.e., every element is at least as large as the previous element. 

The goal is to find the minimum number of moves required, where each move increases 
the value of any array element by one.

Parameters:
----------
n : int
    The size of the array. 
    Constraints: 1 ≤ n ≤ 2 x 10^5

arr : List[int]
    The contents of the array.
    Constraints: 1 ≤ arr[i] ≤ 10^9 for each element in the array.

Returns:
-------
int
    The minimum number of moves required to make the array increasing.

Example:
--------
>>> increasing_array(5, [3, 2, 5, 1, 7])
5

This is because, we need to increase the second number from 2 to 3 (1 move), 
and the fourth number from 1 to 5 (4 moves), thus a total of 5 moves is required 
to make the array increasing.

Note:
-----
As the size of the array `n` can be up to 2 x 10^5, an efficient solution is expected 
to solve this problem within the time limit. Be careful with solutions that have a 
time complexity of O(n^2) or worse, as they might not be efficient enough to handle 
larger inputs within a reasonable time frame.
"""

from typing import List

def increasing_array(n: int, arr: List[int]) -> int:
    #TODO Implement this function
    pass
