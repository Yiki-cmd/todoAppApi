from app.models.base import BaseDoc
from app.models.user import User
from app.models.task import Task

from typing import ClassVar, Optional, List
frome beanie import Link
from pydantic import field
from pymongo import ASCENDING, IndexModel



class Project(BaseDoc):
    name: str = Field(default=str, alias="name")
    description: optional[str] = Field(default=None, alias="description")
    owner: Link(user) = Field(..., alias="owner")
    members: optional[list[link[user]]]= Field(default=None, alias="members")
    tasks: optional[list[link[task]]] = Field(default=None, alias="tasks")
    
    class Settings:
        name: ClassVar[str] = "projects"
        indexes: ClassVar[list[IndexModel]] = [
            IndexModel([("owner", ASCENDING)]),
            IndexModel([("createdAt", ASCENDING)])
        ]
