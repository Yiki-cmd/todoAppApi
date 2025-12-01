from typing import ClassVar

from pydantic import Field

from app.models.base import BaseDoc


class Task(BaseDoc):
    name: str = Field(default=str, alias="name")
    email: str = Field(default=str, alias="email")
    password: str = Field(default=str, alias="password")
    message: str = Field(default=str, alias="message")

    class Settings:
        name: ClassVar[str] = "task"
        index: ClassVar[list[IndexModel]] = [IndexModel([("createdAt", ASCENDING)])]
