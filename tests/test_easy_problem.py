from questions.easy_problem import is_easy_problem 

def test_is_easy_problem():
    assert is_easy_problem([1]) is False, "Test 1 failed"
    assert is_easy_problem([0, 0, 0, 1, 0]) is False, "Test 2 failed"
    assert is_easy_problem([0, 1, 0, 0, 0, 0]) is False, "Test 3 failed"
    assert is_easy_problem([1, 1, 1, 1, 1]) is False, "Test 4 failed"
    assert is_easy_problem([1] + [0]*99) is False, "Test 5 failed"
    assert is_easy_problem([0]) is True, "Test 6 failed"
    assert is_easy_problem([0, 0, 0, 0, 0]) is True, "Test 7 failed"
    assert is_easy_problem([0]*100) is True, "Test 8 failed"
