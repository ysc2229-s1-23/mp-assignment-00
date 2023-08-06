from questions.trailing_zeros import trailing_zeros 

def test_trailing_zeros():
    assert trailing_zeros(1) == 0, "Test 1 failed"
    assert trailing_zeros(5) == 1, "Test 2 failed"
    assert trailing_zeros(20) == 4, "Test 3 failed"
    assert trailing_zeros(100) == 24, "Test 4 failed"
    assert trailing_zeros(25) == 6, "Test 5 failed"
    assert trailing_zeros(26) == 6, "Test 6 failed"
    assert trailing_zeros(1000000000) == 249999998, "Test 7 failed"
    assert trailing_zeros(850915850) == 212728957, "Test 8 failed"
