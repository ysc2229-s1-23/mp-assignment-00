from questions.longest_repetitions import longest_repetitions

def test_longest_repetitions():
    # Basic tests
    assert longest_repetitions("ATTCGGGA") == 3
    assert longest_repetitions("AAAA") == 4
    assert longest_repetitions("ACGT") == 1

    assert longest_repetitions("A") == 1  
    assert longest_repetitions("AAAACGTTTT") == 4
    assert longest_repetitions("ACGT"*10**5 + "A") == 2
    assert longest_repetitions("A"*10**6) == 10**6 
