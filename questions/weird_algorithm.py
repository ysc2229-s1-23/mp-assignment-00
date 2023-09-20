"""
Implements the weird algorithm as described below: 

The algorithm takes as input a positive integer n. If n is even, 
the algorithm divides it by two, and if n is odd, the algorithm 
multiplies it by three and adds one. The algorithm repeats this, 
until n is one.

Parameters:
----------
n : int
    A positive integer to which the weird algorithm is applied. 
    Constraints: 1 ≤ n ≤ 10^6

Returns:
-------
List[int]
    A list that contains all values of n during the algorithm execution.

Example:
--------
>>> weird_algorithm(3)
[3, 10, 5, 16, 8, 4, 2, 1]

Here, for n=3, the sequence is as follows: 
3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
"""
from typing import List

def weird_algorithm(n : int) -> List[int]:
    res = []
    while n != 1:
        res.append(n)
        if  n % 2 == 0:
            n = n // 2
        else:
            n = 3* n + 1
    return res + [1]
