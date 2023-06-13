import os

import pytest
from requests.exceptions import HTTPError

from models.user import User
from utils.helpers import get_github_user_info, get_freshdesk_user_info, create_contact, update_contact


@pytest.fixture
def mock_env_github(monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "")


@pytest.fixture
def mock_env_freshdesk(monkeypatch):
    monkeypatch.setenv("FRESHDESK_TOKEN", "")


def test_get_github_info_contains_login_property():
    user_github = get_github_user_info()
    assert user_github.get("login") is not None


def test_raise_exception_github(mock_env_github):
    with pytest.raises(HTTPError):
        _ = get_github_user_info()


def test_get_freshdesk_account_domain_property():
    user_github = get_freshdesk_user_info(type_account="account")
    assert user_github.get("account_domain") is not None


def test_raise_exception_freshdesk_get(mock_env_freshdesk):
    with pytest.raises(HTTPError):
        _ = get_freshdesk_user_info(type_account="account")


def test_create_user_fresh_desk():
    user_right = User(name="mock_name", description="mock-description", email="mock_user_testing@gmail.com",
                      type_user="github")
    user_created = create_contact(user_right)
    assert user_created.get("name") is not None


def test_raise_exception_freshdesk_post(mock_env_freshdesk):
    user_right = User(name="mock_name", description="mock-description", email="mock-description",
                      type_user="github")
    with pytest.raises(HTTPError):
        _ = create_contact(user_right)


def test_update_user_fresh_desk():
    user_right = User(name="mock_name", description="mock-description", type_user="freshdesk",
                      id_freshdesk=150025374161, email="sample@gmail.com")
    user_updated = update_contact(user_right.id, user_right)
    assert user_updated.get("name") is not None


def test_raise_exception_freshdesk_update(mock_env_freshdesk):
    user_right = User(name="mock_name", description="mock-description", email="mock-description",
                      type_user="freshdesk", id_freshdesk=1231245)
    with pytest.raises(HTTPError):
        _ = update_contact(user_right.id, user_right)