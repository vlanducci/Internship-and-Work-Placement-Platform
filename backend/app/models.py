from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer

class Base(DeclarativeBase):
  pass

class FrameworkTest(Base):
  __tablename__ = "framework_test"

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  message: Mapped[str] = mapped_column(String(200))