from datetime import datetime
from sqlalchemy import TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base

class UserModel(Base):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password :Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=False)



class RefreshSessionModel(Base):
    __tablename__ = "refresh_session"
    id:Mapped[int] = mapped_column(primary_key=True)
    refresh_token:Mapped[str] = mapped_column(unique=True)
    expires:Mapped[int]
    created:Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=func.now())
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))