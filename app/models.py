from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int
    is_active: bool = True

def is_adult(user: User) -> bool:
    return user.age >= 18