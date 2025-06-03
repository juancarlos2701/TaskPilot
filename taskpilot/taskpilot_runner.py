"""TaskPilot runner module for orchestrating the action items extraction
and ticket creation pipeline."""

from agents import Runner, trace, gen_trace_id
from agents.result import RunResult
from local_agents import create_action_items_agent, create_tickets_creator_agent
from utils.models import ActionItemsList


class TaskPilotRunner:
    """
    Orchestrates the process of extracting action items from meeting transcripts
    and creating tickets.
    """

    def __init__(self):
        """
        Initialize the TaskPilotRunner with required agents.
        """
        self.action_items_extractor = create_action_items_agent()
        self.tickets_creator = create_tickets_creator_agent()

    async def run(self, meeting_transcript: str) -> RunResult:
        """
        Process a meeting transcript to extract action items and create tickets.

        :param meeting_transcript: Text content of the meeting transcript
        :return: Result of the processing pipeline
        """
        trace_id = gen_trace_id()
        print(f"Starting TaskPilot run... (Trace ID: {trace_id})")
        print(
            f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
        )

        with trace("TaskPilot run", trace_id=trace_id):

            # TODO: Flow shall be changed to the following:
            # 1. Get existing projects and action items (from Jira, Notion, etc.)
            # 2. Provide existing projects and action items to ActionItemsExtractor for it to extract action items corresponding to existing projects and action items.
            # 3. Provide the extracted action items to TicketsCreator for it to create tickets.
            # 4. Return summary of actions from the TicketsCreator eg. which tickets were created, which tickets and projects were updated, which tickets were deleted.

            # 1. Extract action items from meeting transcript
            action_items = await self._extract_action_items(meeting_transcript)

            # 2. Create tickets from action items
            tickets = await self._create_tickets(action_items)

            # 3. Return the results
            # TODO: Return the results

    async def _extract_action_items(self, meeting_transcript: str) -> ActionItemsList:
        """
        Extract action items from the meeting transcript using an AI agent.

        :param meeting_transcript: Text content of the meeting transcript
        :return: List of extracted action items
        """
        result = await Runner.run(
            self.action_items_extractor, input=meeting_transcript
        )
        final_output = result.final_output_as(ActionItemsList)
        return final_output

    async def _create_tickets(self, action_items: ActionItemsList) -> str:
        """
        Create tickets from the extracted action items using an AI agent.

        :param action_items: List of action items to convert into tickets
        :return: String representation of created tickets
        """
        instruction = """"""
        result = await Runner.run(
            self.tickets_creator, input=instruction, context=action_items
        )
        return result.final_output_as(str)
