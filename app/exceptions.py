class UserAlreadyExistsError(Exception):
    """User already exist"""
    pass

class UserNotFoundError(Exception):
    """User not found"""
    pass