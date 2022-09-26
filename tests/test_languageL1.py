from modules import languageL1

def test_language_1():
    assert languageL1.get_is_accepted("0") == True
    assert languageL1.get_is_accepted("1") == True
    assert languageL1.get_is_accepted("00") == True
    assert languageL1.get_is_accepted("01") == False
    assert languageL1.get_is_accepted("10") == False
    assert languageL1.get_is_accepted("11") == True
    assert languageL1.get_is_accepted("000") == True
    assert languageL1.get_is_accepted("001") == False
    assert languageL1.get_is_accepted("010") == True
    assert languageL1.get_is_accepted("011") == False
    assert languageL1.get_is_accepted("100") == False
    assert languageL1.get_is_accepted("101") == True
    assert languageL1.get_is_accepted("110") == False
    assert languageL1.get_is_accepted("111") == True
    assert languageL1.get_is_accepted("0000") == True
    assert languageL1.get_is_accepted("0001") == False
    assert languageL1.get_is_accepted("0010") == True
    assert languageL1.get_is_accepted("0011") == False
    assert languageL1.get_is_accepted("0100") == True
    assert languageL1.get_is_accepted("0101") == False
    assert languageL1.get_is_accepted("0110") == True
    assert languageL1.get_is_accepted("0111") == False
    assert languageL1.get_is_accepted("1000") == False
    assert languageL1.get_is_accepted("1001") == True
    assert languageL1.get_is_accepted("1010") == False
    assert languageL1.get_is_accepted("1011") == True
    assert languageL1.get_is_accepted("1100") == False
    assert languageL1.get_is_accepted("1101") == True
    assert languageL1.get_is_accepted("1110") == False
    assert languageL1.get_is_accepted("1111") == True