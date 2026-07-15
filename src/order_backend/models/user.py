from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    email: str
    password: str
    is_active: bool = True
