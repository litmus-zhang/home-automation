# conftest.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import devices, users  # Import your database models
from app.config import get_test_db_url  # Your test database configuration

@pytest.fixture(scope="module")
def db():
    # Set up a SQLite in-memory database for testing
    db_url = get_test_db_url()
    engine = create_engine(db_url)
    
    # Create tables
    Base.metadata.create_all(engine)
    
    # Create a session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    yield session
    
    # Teardown: Close the session and drop tables
    session.close()
    Base.metadata.drop_all(engine)
