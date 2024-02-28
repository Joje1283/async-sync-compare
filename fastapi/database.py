from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "mysql://root:root_password@mysql/my_database"
ASYNC_DATABASE_URL = "mysql+aiomysql://root:root_password@mysql/my_database"


async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
)


Base = declarative_base()
# async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
async_session = sessionmaker(
    async_engine, class_=AsyncSession, autoflush=False, autocommit=False
)


async def get_async_session() -> AsyncSession:
    """
    This function is used to get an async session from the database
    """
    async with AsyncSession(async_engine) as session:
        yield session


def get_session() -> Session:
    """
    This function is used to get a session from the database
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
