import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.automap import automap_base

schema = os.environ.get("POSTGRES_SCHEMA", "postgres")
user = os.environ.get("POSTGRES_USER", "user")
host = os.environ.get("POSTGRES_HOST", "localhost")
port = os.environ.get("POSTGRES_PORT", 5432)
password = os.environ.get("POSTGRES_PASSWORD", "password")

SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{schema}')

# engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{schema}")
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
# 
# Base = automap_base()
# Base.prepare(engine, reflect=True)
# 
# # Tables
# Astronauts = Base.classes.astronauts
# 
# def get_astronauts():
#   return session.query(Astronauts).all()
