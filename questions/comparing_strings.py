
"""
Implements the 'Compare Strings with Backspaces' algorithm as described below:

Given two strings that may contain '#', which is a backspace. The goal is to check if the two strings are equal
when both are typed into empty text editors. '#' means a backspace character. This means that string after
processing backspaces could be different from the original string.

Parameters:
str1 : str
The first string to compare. This string consists of lowercase English letters and '#'.
Constraints: 1 ≤ len(str1) ≤ 1000

str2 : str
The second string to compare. This string consists of lowercase English letters and '#'.
Constraints: 1 ≤ len(str2) ≤ 1000

Returns:
bool
True if the strings are equal after processing backspaces and False otherwise.

Example:
compare_strings("xy#z", "xzz#")
True

compare_strings("xy#z", "xyz#")
False

compare_strings("xp#", "xyz##")
True

compare_strings("xywrrmp", "xywrrmu#p")
True

Note:
The backspace character '#' when applied results in the removal of the preceding character in the string. If there
is no preceding character, it has no effect.
"""

def compare_strings(str1: str, str2: str) -> bool:
    #TODO Implement this function
    pass
