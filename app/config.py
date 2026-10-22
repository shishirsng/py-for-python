import os
from dotenv import load_dotenv

load_dotenv()   # .env file padh kar environment mein daal deta hai

APP_NAME = os.getenv("APP_NAME", "Default App")   # default value agar .env mein na ho
DEBUG = os.getenv("DEBUG", "False") == "True"

def intro() -> None:
    print(f"Welcome to {APP_NAME}!")