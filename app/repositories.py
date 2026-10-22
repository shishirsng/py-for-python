from typing import Optional
from app.exceptions import UserAlreadyExistsError
from app.models import User

class UserRepository:
    def __init__(self):
        self.users: list[User] = []   # pretend this is a database table

    def save(self, user: User) -> None:
        if self.find_by_email(user.email) is not None:
            raise UserAlreadyExistsError(f"The user with email {user.email} already exists.")
        self.users.append(user)

    def find_by_email(self, email: str) -> Optional[User]:
        for user in self.users:
            if user.email == email:
                return user
        return None