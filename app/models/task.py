from datetime import datetime
from typing import ClassVar

from beanie import Link
from pydantic import Field
from pymongo import ASCENDING, IndexModel

from app.models.base import BaseDoc
from app.models.enums import TaskStatus
from app.models.project import Project
from app.models.user import User


class Task(BaseDoc):
    title: str = Field(..., alias="title")
    description: str | None = Field(default=None, alias="description")
    status: TaskStatus = Field(default=TaskStatus.PENDING, alias="status")
    project: Link[Project] = Field(..., alias="project")
    assignee: Link[User] | None = Field(default=None, alias="assignee")
    due_date: datetime | None = Field(default=None, alias="dueDate")

    class Settings:
        name: ClassVar[str] = "tasks"

    indexes: ClassVar[list[IndexModel]] = [
        IndexModel([("project", ASCENDING)]),
        IndexModel([("assignee", ASCENDING)]),
        IndexModel([("status", ASCENDING)]),
    ]
