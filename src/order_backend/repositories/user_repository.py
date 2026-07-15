class UserRepository:
    """Minimal in-memory user store used by the application layer."""

    def __init__(self):
        self._users_by_email = {}

    def add(self, user):
        self._users_by_email[user.email.lower()] = user

    def get_by_email(self, email):
        return self._users_by_email.get(email.lower())
