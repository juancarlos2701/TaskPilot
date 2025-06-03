"""Agent implementation for creating tickets from action items."""

from agents import Agent
from utils.config_parser import Config

AGENT_PROMPT = """
"""


def create_tickets_creator_agent() -> Agent:
    """Create an agent that creates tickets given action items."""
    return Agent(
        name="Tickets Creator",
        instructions=AGENT_PROMPT,
        model=Config.get().agents.model,
    )
