from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg

# Write DB (via HAProxy)
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5435/appdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
