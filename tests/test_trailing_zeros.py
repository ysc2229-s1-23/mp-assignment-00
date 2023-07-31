from questions.trailing_zeros import trailing_zeros  # replace "your_module" with the name of your actual module

def test_trailing_zeros():
    assert trailing_zeros(1) == 0

    assert trailing_zeros(5) == 1

    assert trailing_zeros(20) == 4

    assert trailing_zeros(100) == 24

    assert trailing_zeros(25) == 6

    assert trailing_zeros(26) == 6

    assert trailing_zeros(1000000000) == 249999998

    assert trailing_zeros(850915850) == 212728957
