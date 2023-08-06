from questions.comparing_strings import compare_strings

def test_is_easy_problem():
    assert compare_strings("xy#z", "xzz#") == True, "Test 1 failed"
    assert compare_strings("xy#z", "xyz#") == False, "Test 2 failed"
    assert compare_strings("xp#", "xyz##") == True, "Test 3 failed"
    assert compare_strings("xywrrmp", "xywrrmu#p") == True, "Test 4 failed"
