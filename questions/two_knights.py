
"""
Implements the 'two knights' algorithm as described below:

This function calculates the number of ways two knights can be placed on a chessboard of varying sizes (from 1x1 to nxn)
so that they do not attack each other. A knight in chess moves in an L-shape - two squares vertically and one square
horizontally, or two squares horizontally and one square vertically. Thus, two knights attack each other if they are in
positions that are two squares away in one direction and one square away in the perpendicular direction.

Parameters:
n : int
The size of the largest chessboard. The function considers all sizes from 1x1 up to nxn.
Constraints: 1 ≤ n ≤ 10,000

Returns:
List[int]
A list of n integers, where each integer represents the number of ways two knights can be placed on a kxk
chessboard (where k varies from 1 to n) without attacking each other.

Example:
two_knights(8)
[0, 6, 28, 96, 252, 550, 1056, 1848]

In a 1x1 chessboard, there are 0 ways to place two knights without them attacking each other.
In a 2x2 chessboard, there are 6 ways to place two knights without them attacking each other, and so on.

Note:
This problem can be solved by using combinatorics and subtracting the positions where the knights attack each other
from all possible positions.
"""
from typing import List

def two_knights(n: int) -> List[int]:
    # TODO: Implement this function
    pass
