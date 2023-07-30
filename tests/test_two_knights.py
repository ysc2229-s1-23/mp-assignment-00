from questions.two_knights import two_knights

def test_two_knights():
    assert two_knights(1) == [0]
    assert two_knights(2) == [0, 6]
    assert two_knights(3) == [0, 6, 28]
    assert two_knights(4) == [0, 6, 28, 96]
    assert two_knights(5) == [0, 6, 28, 96, 252]

    assert two_knights(10**3) != None 
    assert two_knights(10000) != None 
    assert len(two_knights(10000)) == 10000 
