"""Data models for TaskPilot application."""

from pydantic import BaseModel


class ActionItem(BaseModel):
    """A task that needs to be completed."""

    title: str
    description: str
    assignee: str
    due_date: str
    start_date: str
    status: str
    priority: str
    labels: list[str]
    project: str
    parent: str
    children: list[str]


class ActionItemsList(BaseModel):
    """A list of action items."""

    action_items: list[ActionItem]
