
"""
Implements the 'beautiful permutations' algorithm as described below:

A permutation of integers 1, 2, ..., n is called "beautiful" if there are no adjacent elements whose difference is 1.
Given an integer n, this function constructs a beautiful permutation if such a permutation exists.

Parameters:
n : int
The integer to construct a beautiful permutation from.
Constraints: 1 ≤ n ≤ 10^6

Returns:
List[int] or str
If a beautiful permutation exists, a list of integers representing the beautiful permutation is returned.
If such a permutation doesn't exist, the string "NO SOLUTION" is returned.

Examples:
beautiful_permutations(5)
[2, 4, 1, 3, 5]

Here, the function returns a beautiful permutation of size 5. The permutation [2, 4, 1, 3, 5] is considered
beautiful because there are no adjacent elements whose difference is 1.

beautiful_permutations(3)
"NO SOLUTION"

Here, the function returns "NO SOLUTION" because a beautiful permutation of size 3 does not exist.

Note:
Remember that for n = 2 or n = 3, there is no possible beautiful permutation, hence the function should return
"NO SOLUTION". For n = 1, the function should return [1] as the single number itself is a valid permutation.
For n > 3, a valid solution does exist. The function should strive to find such a valid solution.
"""

from typing import Union, List

def beautiful_permutations(n: int) -> Union[str, List[int]]:
    # TODO: Implement this function
    pass
