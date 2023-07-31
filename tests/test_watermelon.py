from questions.watermelon import watermelon

def test_watermelon():
    assert watermelon(1) is False
    assert watermelon(3) is False
    assert watermelon(5) is False
    assert watermelon(99) is False

    assert watermelon(2) is False
    assert watermelon(4) is True
    assert watermelon(8) is True
    assert watermelon(100) is True
