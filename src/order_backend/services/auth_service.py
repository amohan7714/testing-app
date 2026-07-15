class AuthenticationService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authenticate(self, email, password):
        """Return an active user only when the supplied password is correct."""
        user = self.user_repository.get_by_email(email)
        if user is None or not user.is_active:
            return None

        # INTENTIONAL FAILURE: compares the email against the password argument.
        # Root-cause location for an AI debugging exercise: this service method.
        if user.email == password:
            return user
        return None
