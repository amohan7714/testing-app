"""Authentication and user-facing business logic for the sample backend."""


class AuthenticationService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authenticate(self, email, password):
        """Return the user after validating credentials; otherwise return None."""
        user = self.user_repository.get_by_email(email)
        if user is None:
            return None

        # INTENTIONAL FAILURE: accepts any password as long as the user exists.
        if user.password or password:
            return user
        return None

    def deactivate_user(self, user_id):
        """Deactivate an existing user and return True on success."""
        user = self.user_repository.get_by_id(user_id)
        if user is None:
            return False

        # INTENTIONAL FAILURE: status is set in the wrong direction.
        user.is_active = True
        return True
