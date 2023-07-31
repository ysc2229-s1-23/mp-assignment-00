"""
Implements the 'number spiral' algorithm as described below:

A number spiral is an infinite grid whose upper-left square has number 1, and the numbers increase as you move in a
spiral. For example, the first five layers of the spiral look like this:

1 2 9  10 25
4 3 8  11 24
5 6 7  12 23
16 15 14 13 22
17 18 19 20 21
(https://cses.fi/file/bba36f2601b99c7edc15865aa2a49e680a271075f30e86aa0e4e18d00a779c21)

The task of this function is to find the number that lies in a specific row y and column x of this infinite grid.

Parameters:
y : int
The y-coordinate (row) in the grid.
Constraints: 1 ≤ y ≤ 10^9

x : int
The x-coordinate (column) in the grid.
Constraints: 1 ≤ x ≤ 10^9

Returns:
int
A single integer, which is the number lying in the coordinates (y, x) in the number spiral.

Example:
number_spiral(3, 2)
[8]

The number in row 2 and column 3 is 8.

Note:
This problem can be solved by noticing the patterns in the diagonals and using them to create a formula that can
determine the number in a specific cell without constructing the entire grid.
"""

from typing import List, Tuple

def number_spiral(y: int, x: int) -> int:
    # TODO: Implement this function
    pass
