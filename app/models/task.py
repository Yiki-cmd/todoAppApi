from typing import ClassVar

from beanie import Link
from pydantic import Field

from app.models.base import BaseDoc
from app.models.enums import TaskStatus
from app.models.project import Project
from app.models.user import User


class Task(BaseDoc):
    name: str = Field(default=str, alias="name")
    email: str = Field(default=str, alias="email")
    password: str = Field(default=str, alias="password")
    message: str = Field(default=str, alias="message")

    class Settings:
         name: ClassVar[str] = "task"
        indexes: ClassVar[list[IndexModel]] = [IndexModel([("createdAt", ASCENDING)])]
