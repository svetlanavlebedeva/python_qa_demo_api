import pytest
import requests


@pytest.mark.parametrize("lang, id_",
                         [('rus', 12),
                          ('urd', 1),
                          ('esp', 31),
                          ('ita', 13),
                          ('zho', 22)])
def test_meow_api(lang, id_):
    query = {'lang': lang,
             'id': id_}

    r = requests.get('https://meowfacts.herokuapp.com/', params=query)
    assert r.status_code == 200
    assert r.json()['data']


@pytest.mark.parametrize('lang', ['rus', 'urd', 'esp', 'ita', 'zho'])
@pytest.mark.parametrize('id_', [12, 1, 31, 13, 22])
def test_meow_api_combo(lang, id_):
    query = {'lang': lang,
             'id': id_}

    r = requests.get('https://meowfacts.herokuapp.com/', params=query)
    assert r.status_code == 200
    assert r.json()['data']
