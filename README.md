# TaskPilot - Meeting Transcript to Tickets
This repository is to create an agentic flow where given the transcript of a meeting it extracts relevant action items and creates corresponding tickets in desired project-management applications (i.e. Jira, Notin,...).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.10+
* Pip
* Virtualenv

### Installing

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/TaskPilot.git
   cd TaskPilot
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv_taskpilot
   source .venv_taskpilot/bin/activate  # On Windows use `.venv_taskpilot\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the application:**
   - Rename the `config.yml.example` file to `config.yml`.
   - Open the `config.yml` file and fill in the required credentials for the services you want to use (e.g., Jira, OpenAI).

     *Note: The project is currently using function-calling for integrations, but it will be updated to use a Jira MCP Server soon.*

## Usage

To run the main application, execute the following command:

```bash
python -m taskpilot.main
```

## Project Structure

Here is an overview of the project's structure and the purpose of each key file:

```
TaskPilot/
├── .gitignore
├── config.yml.example
├── README.md
├── requirements.txt
└── taskpilot/
    ├── main.py
    ├── taskpilot_runner.py
    ├── local_agents/
    │   ├── action_items_extractor.py
    │   └── tickets_creator.py
    └── utils/
        ├── agents_tools.py
        ├── config_parser.py
        ├── jira_interface_functions.py
        └── models.py
```

*   **`taskpilot/`**: The main package containing the application's source code.
    *   **`main.py`**: The entry point for the application. It orchestrates the overall workflow.
    *   **`taskpilot_runner.py`**: Contains the core logic for executing the agentic flow, from processing the transcript to creating tickets.
    *   **`local_agents/`**: This directory holds the specialized agents responsible for specific tasks.
        *   `action_items_extractor.py`: This agent is responsible for reading a meeting transcript and identifying actionable tasks or to-dos.
        *   `tickets_creator.py`: This agent takes the extracted action items and creates tickets in the configured project management tool.
    *   **`utils/`**: A collection of utility modules that provide helper functions and classes to the rest of the application.
        *   `agents_tools.py`: Defines tools that can be used by the agents, such as the Jira functions.
        *   `config_parser.py`: Handles reading and parsing the `config.yml` file.
        *   `jira_interface_functions.py`: Contains the functions for interacting with the Jira API (e.g., creating tickets).
        *   `models.py`: Defines the Pydantic models used for data validation and structuring throughout the application.
*   **`config.yml.example`**: An example configuration file. Users should rename this to `config.yml` and fill in their specific details.
*   **`requirements.txt`**: A list of all the Python dependencies required to run the project.
*   **`README.md`**: This file, providing documentation for the project.

