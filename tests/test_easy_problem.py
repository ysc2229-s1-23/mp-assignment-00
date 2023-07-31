from questions.easy_problem import is_easy_problem 

def test_is_easy_problem():
    assert is_easy_problem([1]) is False
    assert is_easy_problem([0, 0, 0, 1, 0]) is False
    assert is_easy_problem([0, 1, 0, 0, 0, 0]) is False
    assert is_easy_problem([1, 1, 1, 1, 1]) is False
    assert is_easy_problem([1] + [0]*99) is False

    assert is_easy_problem([0]) is True
    assert is_easy_problem([0, 0, 0, 0, 0]) is True
    assert is_easy_problem([0]*100) is True
