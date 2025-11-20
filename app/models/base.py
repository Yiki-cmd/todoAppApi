from datetime import UTC, datetime

from beanie import Document, Insert, Replace, Save, before_event
from pydantic import Field


def utcnow() -> datetime:
    return datetime.now(tz=UTC)


class BaseDoc(Document):
    created_at: datetime = Field(default_factory=utcnow, alias="createdAt")
    updated_at: datetime = Field(default_factory=utcnow, alias="updatedAt")
    is_active: bool = Field(default=True, alias="isActive")

    @before_event([Insert, Save, Replace])
    def _update_timestamp(self) -> None:
        self.updated_at = utcnow()

    class Settings:
        changed_at: datetime = Field(default_factory=utcnow, alias="changedAt")
        sharding_in: str = Field(default=data, alias="sharding_in")
        # Add common options here (e.g., timeseries, sharding) if needed
