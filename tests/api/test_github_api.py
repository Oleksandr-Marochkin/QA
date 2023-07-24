import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("bunenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 42
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_can_not_be_found(github_api):
    r = github_api.search_repo("NightVz_repo_not_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_can_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api_ind
def test_search_emoji_positive(github_api):
    r = github_api.search_emoji()
    assert "1f4af.png" in r["100"]


@pytest.mark.api_ind
def test_search_emoji_negative(github_api):
    r = github_api.search_emoji()
    assert ["1234"] != "Not Found"


@pytest.mark.api_ind
def test_commit_email_positive(github_api):
    r = github_api.get_commits("Oleksandr-Marochkin", "QA", "master")
    assert r["commit"]["author"]["email"] == "alexander.dec@gmail.com"


@pytest.mark.api_ind
def test_commit_author_positive(github_api):
    r = github_api.get_commits("Oleksandr-Marochkin", "QA", "master")
    assert r["commit"]["author"]["name"] == "Oleksandr Marochkin"
