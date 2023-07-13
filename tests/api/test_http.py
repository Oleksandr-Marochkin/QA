import pytest
import requests


@pytest.mark.http
def test_first_requesr():
    r = requests.get("https://api.github.com/zen")
    print(f"Response is{r.text}")


@pytest.mark.http
def test_second_requesr():
    r = requests.get("https://api.github.com/users/defunkt")
    body = r.json()
    headers = r.headers
    assert body["name"] == "Chris Wanstrath"
    assert r.status_code == 200
    assert headers["Server"] == "GitHub.com"


@pytest.mark.http
def test_status_code_request():
    r = requests.get("https://api.github.com/users/sergii_butenko")
    assert r.status_code == 404
