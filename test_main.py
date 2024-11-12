from main import data_SMHI
from datetime import datetime
import pytest

def test_API_response():
    df, code = data_SMHI()
    assert code == 200, f"Expected status code 200, but got {code}"

def test_unit():
    df, code, samlad_data_dict = data_SMHI()
    
    # Check date format
    date_str = samlad_data_dict["date"]
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        pytest.fail("Incorrect date format")

     
    # Test hour format 


    # Check rainOrsnow boolean



    