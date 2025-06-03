"""Data models for TaskPilot application."""

from typing import Optional
from pydantic import BaseModel


class ActionItem(BaseModel):
    """A task that needs to be completed."""

    title: str
    description: str
    assignee: str
    status: str
    due_date: Optional[str] = None
    start_date: Optional[str] = None
    priority: Optional[str] = None
    labels: Optional[list[str]] = None
    project: Optional[str] = None
    parent: Optional[str] = None
    children: Optional[list[str]] = None


class ActionItemsList(BaseModel):
    """A list of action items."""

    action_items: list[ActionItem]
