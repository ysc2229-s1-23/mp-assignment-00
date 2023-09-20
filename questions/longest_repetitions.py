
"""
Implements the 'longest repetitions' algorithm as described below:

Given a DNA sequence - a string consisting of characters A, C, G, and T, this function
finds the longest repetition in the sequence. This is a maximum-length substring
containing only one type of character.

Parameters:
s : str
A DNA sequence, represented as a string consisting of characters 'A', 'C', 'G', and 'T'.
Constraints: The length of the string, 1 ≤ n ≤ 10^6

Returns:
int
The length of the longest repetition in the DNA sequence.

Example:
longest_repetitions("ATTCGGGA")
3

In the given DNA sequence "ATTCGGGA", the longest repetition is 'GGG' which has a length of 3.

Note:
This problem has a straightforward solution by iterating through the string and maintaining
a count of the maximum repeating characters until the character changes. However, the
solution needs to handle edge cases such as when the string is empty or consists of only
a single type of character.
"""
def longest_repetitions(s: str) -> int:

    if len(s) == 0:
        return 0

    cur = ""
    cnt = 0
    max_cnt = 0

    for char in s:
        if char == cur:
            cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)
            cnt = 1
            cur = char

    max_cnt = max(cnt, max_cnt)
    return  max_cnt
