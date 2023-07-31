from questions.long_words import long_words

def test_long_words():
    assert long_words("localization") == "l10n"
    assert long_words("internationalization") == "i18n"
    assert long_words("word") == "word"
    assert long_words("abbreviation") == "a10n"
    assert long_words("characters") == "characters"
    assert long_words("a") == "a"
    assert long_words("ab") == "ab"
    assert long_words("abc") == "abc"
    assert long_words("abcdefghijk") == "a9k"

    assert long_words("aaaaaaaaaaa") == "a9a"
    assert long_words("abbbbbbbbbb") == "a9b"
    assert long_words("bbbbbbbbbba") == "b9a"
    assert long_words("Localization") == "L10n"
    assert long_words("a"*101) == "a99a" 
    assert long_words("") == ""
