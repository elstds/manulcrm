from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String
from app.core.models import Base

class User(Base):
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)