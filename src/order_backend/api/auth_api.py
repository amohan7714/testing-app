def login(authentication_service, payload):
    """Handle a simplified login request and return a response dictionary."""
    user = authentication_service.authenticate(payload["email"], payload["password"])
    if user is None:
        return {"status": 401, "body": {"message": "Invalid credentials"}}
    return {"status": 200, "body": {"user_id": user.user_id}}
