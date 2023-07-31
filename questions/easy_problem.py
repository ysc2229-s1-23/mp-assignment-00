"""
Implements the 'Is it an easy problem?' algorithm as described below:

You are preparing a tournament and you have a problem that you'd like to use. You asked n people about their opinions
on the problem. Each person answered whether this problem is easy (represented as 0) or hard (represented as 1).

This function determines if the problem is easy or hard based on the responses. If at least one person has answered
that the problem is hard (represented as 1), the problem is considered hard.

Parameters:
arr : List[int]
A list of n integers, each integer is either 0 or 1. If i-th integer is 0, then i-th person thinks that
the problem is easy; if it is 1, then i-th person thinks that the problem is hard.
Constraints: 1 ≤ n ≤ 100

Returns:
bool
True if all people think the problem is easy and False otherwise.

Example:
is_easy_problem([0, 0, 0, 1, 0])
False

is_easy_problem([0, 0, 0, 0, 0])
True

Note:
If at least one person thinks the problem is hard, the problem is considered hard.
"""

from typing import List

def is_easy_problem(arr: List[int]) -> bool:
    #TODO Implement this function
    pass
