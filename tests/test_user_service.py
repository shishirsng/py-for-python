import pytest
from app.exceptions import UserAlreadyExistsError, UserNotFoundError
from app.models import User, is_adult
from app.repositories import UserRepository
from app.services.user_service import UserService


@pytest.fixture
def repo():
    return UserRepository()           # har test ko nayi, khaali repository


@pytest.fixture
def service(repo, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)       # log file temp folder mein banegi, tumhare project mein nahi
    return UserService(database=repo)


def test_is_adult_true():
    user = User(name="Asha", email="asha@example.com", age=90)
    assert is_adult(user) is True


def test_is_adult_false():
    user = User(name="Ravi", email="ravi@example.com", age=10)
    assert is_adult(user) is False


def test_find_by_email_returns_none_when_missing(repo):
    assert repo.find_by_email("nobody@example.com") is None


def test_register_user_saves_user(service, repo):
    user = service.register_user(name="Asha", email="asha@example.com", age=90)
    assert repo.find_by_email("asha@example.com") == user


def test_register_duplicate_raises_error(service):
    service.register_user(name="Asha", email="asha@example.com", age=90)
    with pytest.raises(UserAlreadyExistsError):
        service.register_user(name="Asha", email="asha@example.com", age=90)


def test_deactivate_user_sets_inactive(service, repo):
    user = service.register_user(name="Asha", email="asha@example.com", age=90)
    service.deactivate_user(user)
    assert repo.find_by_email("asha@example.com").is_active is False


def test_deactivate_unknown_user_raises_error(service):
    ghost = User(name="Ghost", email="ghost@example.com", age=30)
    with pytest.raises(UserNotFoundError):
        service.deactivate_user(ghost)