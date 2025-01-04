from os import environ

try:
    from dotenv import load_dotenv

    load_dotenv()
    load_dotenv(".env.example")
except ImportError:
    pass

DATABASE_URL = environ["DATABASE_URL"]
JWT_ALGORITHM = environ["JWT_ALGORITHM"]
JWT_SECRET = environ["JWT_SECRET"]
