from main import data_SMHI
from datetime import datetime
import pytest


df, code, samlad_data_dict = data_SMHI()
def test_API_response():
    assert code == 200, f"Expected status code 200, but got {code}"

def test_date_format():
    date_str = samlad_data_dict["date"]
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        pytest.fail("Incorrect date format")

def test_hour():
    hour = samlad_data_dict["hour"]
    assert isinstance(hour, int) and 0 <= hour <= 23, "Hour format is incorrect"

def test_rain_snow_boolean():
    rain_or_snow = samlad_data_dict["rainOrSnow"]
    assert isinstance(rain_or_snow, bool), "Rain or snow, error value"



    