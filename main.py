from app.config import intro
from app.models import is_adult
from app.repositories import UserRepository
from app.services.user_service import UserService
from app.exceptions import UserAlreadyExistsError

def main():
    intro()

    repo = UserRepository()
    service = UserService(database=repo)
    user = None
    try:
        user = service.register_user(name="Asha", email="asha@example.com", age=90)
        user = service.register_user(name="Asha", email="asha@example.com", age=90)  # dobara, same run
    except UserAlreadyExistsError as e:
        print(f"Error: {e}")
        
    if user is not None:
        b = is_adult(user)
        print(f"Is {user.name} an adult? {'Yes' if b else 'No'}")
    else:
        print("User register nahi ho paya, is_adult skip kar rahe hain")

    found = repo.find_by_email("asha@example.com")
    print(found)

if __name__ == "__main__":
    main()
