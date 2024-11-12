from main import data_SMHI

def API_test_response():
    code, df = data_SMHI()
    assert code == 200