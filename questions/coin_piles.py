"""
Implements the 'coin piles' algorithm as described below:

You are given two coin piles containing a and b coins respectively. On each move, you can either remove one coin
from the first pile and two coins from the second pile, or two coins from the first pile and one coin from the second pile.

The task of this function is to efficiently find out if you can empty both the piles.

Parameters:
a : int
The number of coins in the first pile.
Constraints: 0 ≤ a ≤ 10^9

b : int
The number of coins in the second pile.
Constraints: 0 ≤ b ≤ 10^9

Returns:
bool
True if you can empty the piles and False otherwise.

Example:
coin_piles(2, 1)
True

coin_piles(2, 2)
False

coin_piles(3, 3)
True

Note:
To check whether we can empty both piles, we first need to ensure that the total number of coins in both piles is divisible
by 3 because in each move, we're effectively removing 3 coins.

Then, since we can't remove more than two coins from a pile in one move, the pile with the smaller number of coins should have
at least one-third of the total number of coins. Otherwise, we would deplete one pile before the other.
"""
def coin_piles(a: int, b: int) -> bool:
    if (a + b) % 3 != 0:
        return False
    
    # pile with the smaller number of coins should have at least one-third of the total number of coins
    if min(a, b) * 2 < max(a, b):
        return False

    return True