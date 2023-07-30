from questions.increasing_array import increasing_array

def test_increasing_array():
    assert increasing_array(5, [3, 2, 5, 1, 7]) == 5
    assert increasing_array(3, [2, 2, 2]) == 0
    assert increasing_array(4, [1, 5, 2, 3]) == 3
    assert increasing_array(1, [1]) == 0

    assert increasing_array(0, []) == 0 
    assert increasing_array(6, [1, 1, 1, 1, 1, 1]) == 0
    assert increasing_array(6, [1, 2, 3, 4, 5, 6]) == 0
    assert increasing_array(6, [6, 5, 4, 3, 2, 1]) == 15
    assert increasing_array(6, [10**6]*6) == 0
    assert increasing_array(6, [10**6 - i for i in range(6)]) == 15
