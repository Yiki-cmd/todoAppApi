from typing import ClassVar

from pydantic import Field
from pymongo import ASCENDING, IndexModel

from app.models.base import BaseDoc


class Project(BaseDoc):
    name: str = Field(default=str, alias="name")
    email: str = Field(default=str, alias="email")
    password: str = Field(default=str, alias="password")
    message: str = Field(default=str, alias="message")

    class Settings:
        name: ClassVar[str] = "projet"
        index: ClassVar[list[IndexModel]] = [IndexModel([("createdAt", ASCENDING)])]
