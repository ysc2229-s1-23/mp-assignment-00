from questions.watermelon import watermelon

def test_watermelon():
    assert watermelon(1) is False, "Test 1 failed"
    assert watermelon(3) is False, "Test 2 failed"
    assert watermelon(5) is False, "Test 3 failed"
    assert watermelon(99) is False, "Test 4 failed"
    assert watermelon(2) is False, "Test 5 failed"
    assert watermelon(4) is True, "Test 6 failed"
    assert watermelon(6) is True, "Test 7 failed"
    assert watermelon(8) is True, "Test 8 failed"
    assert watermelon(10) is True, "Test 9 failed"
    assert watermelon(18) is True, "Test 10 failed"
    assert watermelon(20) is True, "Test 11 failed"
    assert watermelon(100) is True, "Test 12 failed"
