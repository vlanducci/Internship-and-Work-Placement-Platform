# database.py
# Configures the asynchronous SQLAlchemy engine and database sessions used to communicate with the PostgreSQL database.

from sqlalchemy.ext.asyncio import (
  create_async_engine,
  async_sessionmaker,
  AsyncSession,
)

from app.config import settings

# Creates the asynchronous database engine using the connection URL defined in the application settings.
engine = create_async_engine(
  settings.database_url,
  echo=True, # Logs SQL statements to the terminal for development and debugging.
)

# Creates a reusable factory for asynchronous database sessions.
AsyncSessionLocal = async_sessionmaker(
  engine,
  class_=AsyncSession,
  expire_on_commit=False, # Keeps loaded object attributes accessible after a commit
)