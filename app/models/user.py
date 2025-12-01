from app.models.base import BaseDoc


class User(BaseDoc):
    class Project(BaseDoc):
    name: str = Field(default=str, alias="name")
    email: str = Field(default=str, alias="email")
    password: str = Field(default=str, alias="password")
    message: str = Field(default=str, alias="message")

    class Settings:
        name: ClassVar[str] = "User"
        indexes: ClassVar[list[IndexModel]] = [IndexModel([("createdAt", ASCENDING)])]
