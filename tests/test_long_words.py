from questions.long_words import long_words

def test_long_words():
    assert long_words("localization") == "l10n", "Test 1 failed"
    assert long_words("internationalization") == "i18n", "Test 2 failed"
    assert long_words("word") == "word", "Test 3 failed"
    assert long_words("abbreviation") == "a10n", "Test 4 failed"
    assert long_words("characters") == "characters", "Test 5 failed"
    assert long_words("a") == "a", "Test 6 failed"
    assert long_words("ab") == "ab", "Test 7 failed"
    assert long_words("abc") == "abc", "Test 8 failed"
    assert long_words("abcdefghijk") == "a9k", "Test 9 failed"
    assert long_words("aaaaaaaaaaa") == "a9a", "Test 10 failed"
    assert long_words("abbbbbbbbbb") == "a9b", "Test 11 failed"
    assert long_words("bbbbbbbbbba") == "b9a", "Test 12 failed"
    assert long_words("Localization") == "L10n", "Test 13 failed"
    assert long_words("a"*101) == "a99a", "Test 14 failed"
    assert long_words("") == "", "Test 15 failed"
