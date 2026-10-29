# models.py
# Defines the SQLAlchemy base class and a test database model used to verify that the application can create and interact with PostgreSQL tables.

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer

# Base class inherited by SQLAlchemy models to register their table definitions.
class Base(DeclarativeBase):
  pass

# Defines a test table used to verify database operations.
class FrameworkTest(Base):
  __tablename__ = "framework_test" # Specifies the name of the database table.

  # Defines the primary key, which uniquely identifies each record.
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  # Defines a text column that stores messages up to 200 characters long.
  message: Mapped[str] = mapped_column(String(200))