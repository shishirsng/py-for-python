from app.models import User
import logging

logger = logging.getLogger(__name__)

def log_call(func):
    def wrapper(*args, **kwargs):
        print("register_user call ho raha hai...")
        result = func(*args, **kwargs)
        print("register_user complete hua")
        return result
    return wrapper

def log_user_action(name: str) -> None:
    with open("user_actions.log", "a") as f:
        f.write(f"Registered: {name}\n")

class UserService:
    def __init__(self, database):
        self.database = database

    @log_call
    def register_user(self, name: str, email: str, age: int) -> User:
        user = User(name=name, email=email, age=age)
        self.database.save(user)
        logger.info(f"Registered user: {user.name}")
        log_user_action(user.name)      # <- yahan call kiya
        return user

    def deactivate_user(self, user: User) -> None:
        user.is_active = False
        self.database.save(user)