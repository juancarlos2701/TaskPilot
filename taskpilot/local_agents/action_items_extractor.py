"""Agent implementation for extracting action items from meeting transcripts."""

from agents import Agent
from utils.config_parser import Config
from utils.models import ActionItemsList

AGENT_PROMPT = """
"""


def create_action_items_agent() -> Agent:
    """Create an agent that gets a meeting transcript and extracts action items."""
    return Agent(
        name="Action Items Extractor",
        instructions=AGENT_PROMPT,
        output_type=ActionItemsList,
        model=Config.get().agents.model,
    )
