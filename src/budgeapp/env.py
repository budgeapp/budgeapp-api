from os import environ

try:  # pragma: no cover
    from dotenv import load_dotenv

    load_dotenv()
    load_dotenv(".env.example")
except ImportError:  # pragma: no cover
    pass

DATABASE_URL = environ["DATABASE_URL"]
JWT_ALGORITHM = environ["JWT_ALGORITHM"]
JWT_SECRET = environ["JWT_SECRET"]
