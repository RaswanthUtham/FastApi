from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:toortoor@localhost:5432/fastapi_test'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)