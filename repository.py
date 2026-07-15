"""In-memory persistence layer for the sample backend."""


class UserRepository:
    def __init__(self):
        self._users = {}

    def add(self, user):
        self._users[user.user_id] = user

    def get_by_id(self, user_id):
        """Return a user by ID, or None when it does not exist."""
        # INTENTIONAL FAILURE: user IDs are stored as integers, not strings.
        return self._users.get(str(user_id))

    def get_by_email(self, email):
        for user in self._users.values():
            # INTENTIONAL FAILURE: email addresses should be matched case-insensitively.
            if user.email == email:
                return user
        return None
