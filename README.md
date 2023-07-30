# Assignment 01 - Data Structures and Algorithms

This repository contains assignments that focus on various data structures and algorithms problems sourced from the CSES problem set.

## Problems

Here are the problems for the assignment:

1. **Weird Algorithm**: Write a function that takes an integer input and implements the weird algorithm. The algorithm is defined as follows: If the number is even, divide it by two. If it's odd, multiply it by three and add one. Continue this process until the number is one. The function should return a list representing the sequence of numbers.
    - Example: `weird_algorithm(3)` should return `[3, 10, 5, 16, 8, 4, 2, 1]`.

2. **Way Too Long Words**: For this problem, write a function that shortens words that are "too long". A word is considered "too long" if it has strictly more than 10 characters. All "too long" words should be shortened to the first and the last character of the word, with the number of characters removed in between them.
    - Example: `long_words("localization")` should return `"l10n"`.

3. **Increasing Array**: Given an array of integers, modify the array so that it is increasing, i.e., every element is at least as large as the previous element. The goal is to find the minimum number of moves required, where each move increases the value of any array element by one.
    - Example: `increasing_array(5, [3, 2, 5, 1, 7])` should return `5`.

4. **Beautiful Permutations**: A permutation of integers 1, 2, ..., n is called "beautiful" if there are no adjacent elements whose difference is 1. The task is to construct a beautiful permutation if one exists.
    - Example: `beautiful_permutations(5)` could return `[2, 4, 1, 3, 5]`.

5. **Longest Repetitions**: Given a DNA sequence - a string consisting of characters A, C, G, and T - find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
    - Example: `longest_repetitions("ATTCGGGA")` should return `3`.

6. **Missing Number**: You are given all numbers between 1, 2, ..., n except one. Your task is to find the missing number.
    - Example: `missing_number([2, 3, 1, 5])` should return `4`.

7. **Number Spiral**: A number spiral is an infinite grid whose upper-left square has number 1. The task is to find out the number in row y and column x.
    - Example: `compute_number_spiral(3, 2)` should return `8`.

8. **Two Knights**: Count the number of ways two knights can be placed on a k×k chessboard so that they do not attack each other.
    - Example: `two_knights(3)` should return `28`.

## Testing

This repository uses `pytest` for unit testing. Each problem has a corresponding test in the `tests` directory. To run the tests, navigate to the repository's root directory and run `pytest`.

## Autograding

We use GitHub Classroom's autograding feature for this assignment. The autograder runs all `pytest` tests and assigns a score based on the number of passing tests.

## Lecture Notes

Please refer to the link in the GitHub Classroom for the lecture notes related to these problems.

## Plagiarism Notice

We use sophisticated plagiarism detection software to ensure the integrity of the assignment submissions. Any attempt to plagiarize will result in a direct fail. Also, remember, using AI such as ChatGPT or similar to generate solutions for assignments is strictly prohibited and may also result in a direct fail.

Remember, the best way to learn programming and problem solving is by doing. Good luck!
