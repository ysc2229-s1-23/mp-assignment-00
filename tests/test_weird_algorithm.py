from questions.weird_algorithm import weird_algorithm

def test_weird_algorithm():
    assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert weird_algorithm(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert weird_algorithm(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    # Edge cases
    assert weird_algorithm(1) == [1] 
    assert weird_algorithm(999999) != None 
    assert isinstance(weird_algorithm(999999), list) 
