from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from db.settings import db_settings

# Create SQLAlchemy Engine using a database URI
# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-sqlalchemy-engine
db_url = db_settings.get_db_url()
db_engine: Engine = create_engine(db_url, pool_size=10, max_overflow=20, pool_pre_ping=True)

# Create a SessionLocal class
# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-sessionlocal-class
SessionLocal: sessionmaker[Session] = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


def get_db():
    """
    Dependency to get a database session.

    https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-dependency
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
