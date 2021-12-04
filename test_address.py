from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("500 Jefferson Street, Mentor, OH 44060") == "Mentor"
    assert extract_city("8741 Sunnyslope Court, Winter Springs, FL 32708") == "Winter Springs"


def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("500 Jefferson Street, Mentor, OH 44060") == "OH"
    assert extract_state("8741 Sunnyslope Court, Winter Springs, FL 32708") == "FL"

def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("500 Jefferson Street, Mentor, OH 44060") == "44060"
    assert extract_zipcode("8741 Sunnyslope Court, Winter Springs, FL 32708") == "32708"



# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])