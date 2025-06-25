"""Utility tools for the agents to use."""

from agents import function_tool
from utils.models import ActionItem
from utils.jira_interface_functions import create_issue


@function_tool
def create_jira_issue(action_item: ActionItem) -> str:
    """
    Create a Jira issue from an ActionItem.

    :param action_item: The action item containing issue details.
    :returns: A message indicating success or error.
    """
    response = create_issue(
        project_key=action_item.project,
        title=action_item.title,
        description=action_item.description,
        issuetype=action_item.issuetype,
        duedate=action_item.due_date,
        assignee_id=None,
        labels=None,
        priority_id=None,
        reporter_id=None,
    )

    if response.ok:
        return f"Successfully created the issue. Response message: {response.text}"
    else:
        return f"There was an error trying to create the issue. Error message: {response.text}"
