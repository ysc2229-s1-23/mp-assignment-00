from questions.number_spiral import number_spiral

def test_number_spiral():
    assert number_spiral(1, 1) == 1
    assert number_spiral(2, 3) == 8
    assert number_spiral(3, 1) == 7

    assert number_spiral(1, 10**9) == 1000000000000000001
    assert number_spiral(10**9, 1) == 1999999998
    assert number_spiral(10**9, 10**9) == 1999999998000000001
