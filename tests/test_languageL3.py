from modules import languageL3


def test_language_3():
    assert languageL3.get_is_accepted("0") == False
    assert languageL3.get_is_accepted("1") == False
    assert languageL3.get_is_accepted("00") == False
    assert languageL3.get_is_accepted("01") == True
    assert languageL3.get_is_accepted("10") == False
    assert languageL3.get_is_accepted("11") == False
    assert languageL3.get_is_accepted("000") == False
    assert languageL3.get_is_accepted("001") == True
    assert languageL3.get_is_accepted("010") == True
    assert languageL3.get_is_accepted("011") == False
    assert languageL3.get_is_accepted("100") == False
    assert languageL3.get_is_accepted("101") == False
    assert languageL3.get_is_accepted("110") == False
    assert languageL3.get_is_accepted("111") == False
    assert languageL3.get_is_accepted("0000") == False
    assert languageL3.get_is_accepted("0001") == True
    assert languageL3.get_is_accepted("0010") == True
    assert languageL3.get_is_accepted("0011") == False
    assert languageL3.get_is_accepted("0100") == True
    assert languageL3.get_is_accepted("0101") == False
    assert languageL3.get_is_accepted("0110") == False
    assert languageL3.get_is_accepted("0111") == True
    assert languageL3.get_is_accepted("1000") == False
    assert languageL3.get_is_accepted("1001") == False
    assert languageL3.get_is_accepted("1010") == False
    assert languageL3.get_is_accepted("1011") == False
    assert languageL3.get_is_accepted("1100") == False
    assert languageL3.get_is_accepted("1101") == False
    assert languageL3.get_is_accepted("1110") == False
    assert languageL3.get_is_accepted("1111") == False
