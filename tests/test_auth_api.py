from src.order_backend.api.auth_api import login
from src.order_backend.models.user import User
from src.order_backend.repositories.user_repository import UserRepository
from src.order_backend.services.auth_service import AuthenticationService


def build_authentication_service():
    repository = UserRepository()
    repository.add(User(1, "user@example.com", "correct-password"))
    return AuthenticationService(repository)


def test_login_accepts_correct_credentials():
    response = login(
        build_authentication_service(),
        {"email": "user@example.com", "password": "correct-password"},
    )

    assert response == {"status": 200, "body": {"user_id": 1}}


def test_login_rejects_wrong_password():
    response = login(
        build_authentication_service(),
        {"email": "user@example.com", "password": "wrong-password"},
    )

    assert response["status"] == 401
