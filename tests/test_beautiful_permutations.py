from questions.beautiful_permutations import beautiful_permutations
from typing import List, Union

def test_beautiful_permutations():
    assert beautiful_permutations(1) == [1], "Test 1 failed"
    assert beautiful_permutations(2) == "NO SOLUTION", "Test 2 failed"
    assert beautiful_permutations(3) == "NO SOLUTION", "Test 3 failed"
    assert beautiful_permutations(4) == [2, 4, 1, 3], "Test 4 failed"
    assert is_beautiful(beautiful_permutations(5)), "Test 5 failed"
    assert is_beautiful(beautiful_permutations(10)), "Test 6 failed"
    assert is_beautiful(beautiful_permutations(20)), "Test 7 failed"
    assert is_beautiful(beautiful_permutations(10**6)), "Test 8 failed"

def is_beautiful(arr: Union[List[int], str]) -> bool:
    if isinstance(arr, str):
        return arr == "NO SOLUTION"
    else:
        return all(abs(arr[i] - arr[i+1]) != 1 for i in range(len(arr)-1))
