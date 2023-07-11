import data_stuff

def my_func():
    result = load_data()
    return result

KNOWN_RETURN = (1, 2, 3)

def test_load_data(mocker):
    mocker.patch('data_stuff.load_data', return_value=KNOWN_RETURN)
    assert my_func() == (1, 2, 3)

