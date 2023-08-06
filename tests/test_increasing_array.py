from questions.increasing_array import increasing_array

def test_increasing_array():
    assert increasing_array(5, [3, 2, 5, 1, 7]) == 5, "Test 1 failed"
    assert increasing_array(3, [2, 2, 2]) == 0, "Test 2 failed"
    assert increasing_array(4, [1, 5, 2, 3]) == 5, "Test 3 failed"
    assert increasing_array(1, [1]) == 0, "Test 4 failed"
    assert increasing_array(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0, "Test 5 failed"
    assert increasing_array(0, []) == 0, "Test 6 failed"
    assert increasing_array(6, [1, 1, 1, 1, 1, 1]) == 0, "Test 7 failed"
    assert increasing_array(6, [1, 2, 3, 4, 5, 6]) == 0, "Test 8 failed"
    assert increasing_array(6, [6, 5, 4, 3, 2, 1]) == 15, "Test 9 failed"
    assert increasing_array(6, [10**6]*6) == 0, "Test 10 failed"
    assert increasing_array(6, [10**6 - i for i in range(6)]) == 15, "Test 11 failed"
    assert increasing_array(10, [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8999999991, "Test 12 failed"
    assert increasing_array(10, [6, 10, 4, 10, 2, 8, 9, 2, 7, 7]) == 31, "Test 13 failed"
    assert increasing_array(200000, [1 for i in range(200000)]) == 0, "Test 14 failed"
    assert increasing_array(1, [329873232]) == 0, "Test 15 failed"