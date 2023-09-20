"""
This function shortens words that are "too long". A word is considered "too long"
if it has more than 10 characters. The shortened version is formed by the first and last 
characters of the word, with the number of characters removed in between.

Parameters:
----------
s : str
    The word to be abbreviated. The word should consist of lowercase Latin letters and 
    have a length between 1 and 100 (both inclusive).

Returns:
-------
str
    The abbreviated version of the word if the word is "too long". If the word is not 
    "too long", the function will return the original word.

Example:
--------
>>> long_words("internationalization")
"i18n"

In this example, the word "internationalization" has more than 10 characters, 
so it is considered "too long". The function therefore returns its abbreviated form "i18n", 
where 'i' and 'n' are the first and last characters, and '18' is the number of characters 
that were omitted in between.
"""

def long_words(s: str) -> str:
    if len(s) > 10:
        return s[0] + str(len(s)-2) + s[-1]
    else:
        return s
