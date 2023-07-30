from questions.beautiful_permutations import beautiful_permutations
from typing import List, Union

def test_beautiful_permutations():
    assert beautiful_permutations(1) == [1]
    assert beautiful_permutations(2) == [2, 1]
    assert beautiful_permutations(3) == "NO SOLUTION"
    assert beautiful_permutations(4) != "NO SOLUTION"
    assert is_beautiful(beautiful_permutations(5))
    assert is_beautiful(beautiful_permutations(10))
    assert is_beautiful(beautiful_permutations(20))
    assert is_beautiful(beautiful_permutations(10**6))

def is_beautiful(arr: Union[List[int], str]) -> bool:
    if isinstance(arr, str):
        return arr == "NO SOLUTION"
    else:
        return all(abs(arr[i] - arr[i+1]) != 1 for i in range(len(arr)-1))
