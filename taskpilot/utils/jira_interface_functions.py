"""Jira interface functions."""

import os
from typing import Optional
import json
from urllib.parse import urljoin
import requests
from requests.auth import HTTPBasicAuth
from utils.config_parser import Config


JIRA_AUTH = HTTPBasicAuth(Config.get().jira.user, str(os.getenv("ATLASSIAN_API_KEY")))


def create_issue(
    project_key: str,
    title: str,
    description: str,
    issuetype: str,
    duedate: Optional[str] = None,
    assignee_id: Optional[str] = None,
    labels: Optional[list[str]] = None,
    priority_id: Optional[str] = None,
    reporter_id: Optional[str] = None,
) -> requests.Response:
    """
    Create a new Jira issue with the specified parameters.

    :param project_key: Key of the Jira project.
    :param title: Summary/title of the issue.
    :param description: Detailed description of the issue.
    :param issuetype: Type of the issue (e.g., Task, Bug).
    :param duedate: Due date for the issue (optional). Shall be in format "YYYY-MM-dd"
    :param assignee_id: ID of the assignee (optional).
    :param labels: List of labels to add to the issue (optional).
    :param priority_id: ID of the priority of the issue (optional).
    :param reporter_id: ID of the reporter of the issue (optional).
    """
    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": title,
            "issuetype": {"name": issuetype},
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": description,
                                "type": "text",
                            }
                        ],
                        "type": "paragraph",
                    }
                ],
                "type": "doc",
                "version": 1,
            },
        }
    }

    if duedate:
        payload["fields"].update({"duedate": duedate})
    if assignee_id:
        payload["fields"].update({"assignee": {"id": assignee_id}})
    if labels:
        payload["fields"].update({"labels": labels})
    if priority_id:
        payload["fields"].update({"priority": {"id": priority_id}})
    if reporter_id:
        payload["fields"].update({"reporter": {"id": reporter_id}})

    endpoint_url = urljoin(Config.get().jira.url_rest_api, "issue")

    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(
        endpoint_url,
        data=json.dumps(payload),
        headers=headers,
        auth=JIRA_AUTH,
        timeout=Config.get().jira.request_timeout,
    )
    return response
