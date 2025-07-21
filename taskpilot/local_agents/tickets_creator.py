"""Agent implementation for creating tickets from action items."""

from agents import Agent
from agents.mcp import MCPServer
from utils.config_parser import Config
# from utils.models import TicketsCreatorResponse

# TODO: update Prompt to tell agent how to use the MCP-server
AGENT_PROMPT = """
You are an assistant that helps by taking actions in Jira. You can take actions in jira using the jira-mcp-server like creating new issues, updating issues, adding comments to issues and more.

You will be given a list of action items and for each action item you shall evaluate what to do in jira. Decide if given action item already has a corresponding issue in any project which needs to be updated, whether a comment shall be added to it, whether its status shall be updated or if there is no corresponding issue create an issue for the action item. For this you shall use the tools provided on the jira-mcp-server.

You shall summarize your actions in a small text.
"""


def create_tickets_creator_agent(mcp_servers: list[MCPServer]) -> Agent:
    """Create an agent that creates tickets given action items."""
    return Agent(
        name="Tickets Creator",
        instructions=AGENT_PROMPT,
        mcp_servers=mcp_servers,
        model=Config.get().agents.model,
    )
