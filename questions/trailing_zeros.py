
"""
Implements the 'trailing zeros' algorithm as described below:

You are given a positive integer n. The task of this function is to calculate the number of trailing zeros in the
factorial of n.

A trailing zero is formed by multiplying a number by 10, which is a product of 2 and 5. Since the number of 2s would
be much more than the number of 5s in the prime factorization of n!, the number of trailing zeros would be
essentially dictated by the number of factors of 5.

Parameters:
n : int
A positive integer.
Constraints: 1 ≤ n ≤ 10^9

Returns:
int
The number of trailing zeros in n!.

Example:
trailing_zeros(20)
4

The factorial of 20 is 2432902008176640000, which has 4 trailing zeros.

Note:
This problem can be solved by calculating the number of factors of 5 in n!, which can be done by repeatedly dividing
n by 5 until it becomes less than 5. The sum of these quotients gives the number of trailing zeros in n!.
"""
def trailing_zeros(n: int) -> int:
    count = 0

    # While n is greater than or equal to 5
    while n >= 5:
        # Divide n by 5 and add to count
        n = n // 5
        count += n

    # Return the count of trailing zeros
    return count