from questions.longest_repetitions import longest_repetitions

def test_longest_repetitions():
    assert longest_repetitions("ATTCGGGA") == 3, "Test 1 failed"
    assert longest_repetitions("AAAA") == 4, "Test 2 failed"
    assert longest_repetitions("ACGT") == 1, "Test 3 failed"
    assert longest_repetitions("") == 0, "Test 4 failed"
    assert longest_repetitions("A") == 1, "Test 5 failed"
    assert longest_repetitions("AAAACGTTTT") == 4, "Test 6 failed"
    assert longest_repetitions("ACGT"*10**5 + "A") == 1, "Test 7 failed"
    assert longest_repetitions("A"*10**6) == 10**6, "Test 8 failed"
