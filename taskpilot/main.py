"""Main entry point for the TaskPilot application."""

import os
import asyncio
from dotenv import load_dotenv

from taskpilot_runner import TaskPilotRunner

load_dotenv()


def load_meeting_transcript_txt(file_path: str) -> str:
    """
    Load and read the contents of a meeting transcript file.

    :param file_path: Path to the meeting transcript file
    :return: Content of the meeting transcript
    """
    meeting_transcript = ""
    try:
        # Using relative path from the script's location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        absolute_file_path = os.path.join(script_dir, file_path)

        with open(absolute_file_path, "r", encoding="utf-8") as file:
            meeting_transcript = file.read()

    except FileNotFoundError:
        print("Error: Could not find the file 'meeting_transcript.txt'")
        print(f"Please ensure the file exists at: {file_path}")

    return meeting_transcript


async def main():
    """
    Main function that serves as the entry point for the application.
    """
    print("TaskPilot application starting...")

    meeting_transcript = load_meeting_transcript_txt("meeting_transcript.txt")

    await TaskPilotRunner().run(meeting_transcript)


if __name__ == "__main__":
    asyncio.run(main())
