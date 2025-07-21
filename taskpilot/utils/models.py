"""Data models for TaskPilot application."""

from typing import Optional
from pydantic import BaseModel


class ActionItem(BaseModel):
    """
    Represents a task that needs to be completed.

    :param title: Short, descriptive title of the action item.
    :param description: Extended description of the action item.
    :param assignee: Name of the person responsible for the action item.
    :param status: Current status of the action item (e.g., "To Do", "In Progress").
    :param issuetype: Type of the action item (e.g., "Task", "Bug", "Story").
    :param project: Project key or name to which the action item belongs.
    :param due_date: Due date for the action item in "YYYY-MM-DD" format, or None if not specified.
    :param start_date: Start date for the action item in "YYYY-MM-DD" format, or None if not specified.
    :param priority: Priority of the action item (e.g., "High", "Medium"), or None if not specified.
    :param parent: Title of the parent action item if this is a subtask, or None.
    :param children: List of titles of child action items if this is a parent task, or None.
    """

    title: str
    description: str
    assignee: str
    status: str
    issuetype: str
    project: Optional[str] = None
    due_date: Optional[str] = None
    start_date: Optional[str] = None
    priority: Optional[str] = None
    parent: Optional[str] = None
    children: Optional[list[str]] = None


class ActionItemsList(BaseModel):
    """A list of action items."""

    action_items: list[ActionItem]


class TicketsCreatorResponse(BaseModel):
    """
    Represents the response returned by the TicketsCreator Agent after attempting to create issues.

    This model contains the following information:
    
    :param action_items: The list of action items that were provided as input for ticket creation.
    :param error_messages: A list of error messages corresponding to action items for which ticket creation failed.
    :param success_messages: A list of success messages for action items for which tickets were successfully created.
    :param text: A summary string describing the overall result of the ticket creation process, including counts of successes and failures and a summary of error messages.
    """
    # TODO: update to provide summary of what the agent did: created issues, comments written, issues updated...
    action_items: list[ActionItem]
    error_messages: list[str]
    success_messages: list[str]
    text: str
