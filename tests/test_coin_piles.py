from questions.coin_piles import coin_piles

def test_coin_piles():
    assert coin_piles(2, 1) is True, "Test 1 failed"
    assert coin_piles(3, 3) is True, "Test 2 failed"
    assert coin_piles(0, 0) is True, "Test 3 failed"
    assert coin_piles(5, 4) is True, "Test 4 failed"
    assert coin_piles(10**9, 2*10**9) is True, "Test 5 failed"
    assert coin_piles(11, 4) is False, "Test 6 failed"
    assert coin_piles(2, 2) is False, "Test 7 failed"
    assert coin_piles(5, 2) is False, "Test 8 failed"
    assert coin_piles(5, 3) is False, "Test 9 failed"
    assert coin_piles(10**9, 10**9 - 1) is False, "Test 10 failed"
