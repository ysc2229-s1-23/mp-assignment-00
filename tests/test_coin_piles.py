from questions.coin_piles import coin_piles

def test_coin_piles():
    assert coin_piles(2, 1) is True
    assert coin_piles(3, 3) is True
    assert coin_piles(0, 0) is True
    assert coin_piles(5, 4) is True
    assert coin_piles(10**9, 2*10**9) is True

    assert coin_piles(2, 2) is False
    assert coin_piles(5, 2) is False
    assert coin_piles(5, 3) is False
    assert coin_piles(10**9, 10**9 - 1) is False
