from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Sydnee", "Zimmerman") == "Zimmerman; Sydnee"
    assert make_full_name("Zechariah", "Olsen") == "Olsen; Zechariah"
    assert make_full_name("Ja-den", "Kirby") == "Kirby; Ja-den"
    assert make_full_name("D.", "Diaz") == "Diaz; D."
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Zimmerman; Sydnee") == "Zimmerman"
    assert extract_family_name("Olsen; Zechariah") == "Olsen"
    assert extract_family_name("Kirby; Ja-den") == "Kirby"
    assert extract_family_name("Diaz; D.") == "Diaz"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Zimmerman; Sydnee") == "Sydnee"
    assert extract_given_name("Olsen; Zechariah") == "Zechariah"
    assert extract_given_name("Kirby; Ja-den") == "Ja-den"
    assert extract_given_name("Diaz; D.") == "D."
    assert extract_given_name("; ") == ""


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])