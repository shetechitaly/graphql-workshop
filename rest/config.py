import os

schema = os.environ.get("POSTGRES_SCHEMA", "postgres")
user = os.environ.get("POSTGRES_USER", "user")
host = os.environ.get("POSTGRES_HOST", "localhost")
port = os.environ.get("POSTGRES_PORT", 5432)
password = os.environ.get("POSTGRES_PASSWORD", "password")

SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{schema}'
