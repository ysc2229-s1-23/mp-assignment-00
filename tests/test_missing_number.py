from questions.missing_number import missing_number

def test_missing_number():
    assert missing_number(5, [2, 3, 1, 5]) == 4, "Test 1 failed"
    assert missing_number(10, [1, 2, 3, 4, 5, 6, 7, 8, 10]) == 9, "Test 2 failed"
    assert missing_number(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10, "Test 3 failed"
    assert missing_number(10, [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1, "Test 4 failed"
    assert missing_number(2, [2]) == 1, "Test 5 failed"
    assert missing_number(2*10**5 + 1, list(range(1, 2*10**5)) + [2*10**5 + 1]) == 2*10**5, "Test 6 failed"
    assert missing_number(2*10**5 + 1, [1] + list(range(3, 2*10**5 + 2))) == 2 , "Test 7 failed" 
    assert missing_number(2*10**5 + 1, list(range(1, 10**5)) + list(range(10**5 + 1, 2*10**5 + 2))) == 10**5, "Test 8 failed"
