from backend import AuthenticationService
from models import User
from repository import UserRepository


def create_service():
    repository = UserRepository()
    repository.add(User(1, "user@example.com", "correct-password"))
    return AuthenticationService(repository), repository


def test_repository_finds_user_by_integer_id():
    _, repository = create_service()
    assert repository.get_by_id(1).email == "user@example.com"


def test_repository_email_lookup_ignores_case():
    service, _ = create_service()
    assert service.authenticate("USER@example.com", "correct-password") is not None


def test_authentication_rejects_incorrect_password():
    service, _ = create_service()
    assert service.authenticate("user@example.com", "wrong-password") is None


def test_deactivate_user_marks_user_inactive():
    service, repository = create_service()
    assert service.deactivate_user(1) is True
    assert repository.get_by_id(1).is_active is False
