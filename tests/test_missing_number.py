from questions.missing_number import missing_number

def test_missing_number():
    assert missing_number(5, [2, 3, 1, 5]) == 4
    assert missing_number(10, [1, 2, 3, 4, 5, 6, 7, 8, 10]) == 9
    assert missing_number(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
    assert missing_number(10, [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1  

    assert missing_number(2, [2]) == 1
    assert missing_number(2*10**5 + 1, list(range(1, 2*10**5)) + [2*10**5 + 1]) == 2*10**5
    assert missing_number(2*10**5 + 1, [1] + list(range(3, 2*10**5 + 2))) == 2  
    assert missing_number(2*10**5 + 1, list(range(1, 10**5)) + list(range(10**5 + 1, 2*10**5 + 2))) == 10**5
