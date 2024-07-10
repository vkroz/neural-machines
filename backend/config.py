import logging
import os
from dotenv import load_dotenv

"""
# Example of using config usage in another module
from luana_engine.utils.config import Config

# Initialize config with a custom .env path
config = Config.get_config(dotenv_path='custom_path/custom.env')

def using_config_values():
    print("Using OpenAI API Key:", config["OPENAI_API_KEY"])
    print("Using Model:", config["MODEL"])
    print("Debug mode:", config.get("DEBUG_MODE", False))

# Access the already initialized config
config = Config.get_config()
"""

logger = logging.getLogger(__name__)


class ConfigError(Exception):
    """Custom exception for configuration errors."""
    pass


class Config:
    _instance = None

    def __init__(self, dotenv_path='.env'):
        """
        Loads configuration settings from a .env file.
        File can be specified by one of the following methods:
        1. dotenv_path parameter
        2. DOTENV_PATH environment variable
        3. Default path: '.env' in current work dir
        If the file is not found, we log a warning and assume that config settings are present in environment variables.
        """
        if dotenv_path is None:
            dotenv_path = os.getenv('DOTENV_PATH', '.env')

        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        else:
            logger.error(
                "Environment file %s not found. We will look for config settings in environment variables",
                dotenv_path)

    def __getitem__(self, key):
        # Fetch value from environment variables
        value = os.getenv(key)
        if value is None:
            raise ConfigError(f"Configuration key '{key}' not found.")
        return value

    def get(self, key, default=None):
        # Fetch value from environment variables with a default
        value = os.getenv(key, default)
        if value is None:
            raise ConfigError(f"Configuration key '{key}' not found and no default value provided.")
        return value

    def __getattr__(self, key):
        # Fetch value from environment variables when accessed as an attribute
        value = os.getenv(key)
        if value is None:
            raise ConfigError(f"Configuration key '{key}' not found.")
        return value

    @staticmethod
    def get_config(dotenv_path=None):
        if Config._instance is None:
            Config._instance = Config(dotenv_path)
        return Config._instance

    @staticmethod
    def reset():
        Config._instance = None
