"""Configuration management module for TaskPilot."""

from pathlib import Path
import yaml
from pydantic import BaseModel


class AgentsConfig(BaseModel):
    """
    Configurations for agents.
    """

    model: str


class JiraConfig(BaseModel):
    """
    Configurations for Jira integration.
    """

    url_rest_api: str
    user: str


class ConfigModel(BaseModel):
    """
    Configuration model for TaskPilot.
    """

    agents: AgentsConfig
    jira: JiraConfig


class Config:
    """
    Singleton configuration manager for TaskPilot.
    """

    _instance: ConfigModel | None = None

    @classmethod
    def load(cls, path: str = "config.yml") -> None:
        """
        Loads the config if it hasn't been loaded yet.

        :param path: Path to the configuration file
        :return: None
        """
        if cls._instance is None:
            with open(Path(path), "r", encoding="utf-8") as config_file:
                raw_config = yaml.safe_load(config_file)
            cls._instance = ConfigModel(**raw_config)

    @classmethod
    def get(cls, path: str = "config.yml") -> ConfigModel:
        """
        Returns the loaded configuration.

        :param path: Path to the configuration file
        :return: Configuration instance
        """
        if cls._instance is None:
            cls.load(path)
        return cls._instance
