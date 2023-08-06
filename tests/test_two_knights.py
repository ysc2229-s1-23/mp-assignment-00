from questions.two_knights import two_knights

def test_two_knights():
    assert two_knights(1) == [0], "Test 1 failed"
    assert two_knights(2) == [0, 6], "Test 2 failed"
    assert two_knights(3) == [0, 6, 28], "Test 3 failed"
    assert two_knights(4) == [0, 6, 28, 96], "Test 4 failed"
    assert two_knights(5) == [0, 6, 28, 96, 252], "Test 5 failed"
    assert two_knights(10**3) != None, "Test 6 failed"
    assert two_knights(10000) != None, "Test 7 failed"
    assert len(two_knights(10000)) == 10000, "Test 8 failed"
