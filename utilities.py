# taskmanager/utilities.py

import logging
from config import config


def setup_logging():
    """Set up logging based on the configuration."""
    logging_config = config.get_logging_config()

    if not logging_config.get("enabled", False):
        return  # Logging is disabled

    # Configure logging
    log_file = logging_config.get("log_file", "task_manager.log")
    log_level = logging_config.get("log_level", "INFO").upper()

    # Map log level string to logging level
    level_mapping = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    log_level = level_mapping.get(log_level, logging.INFO)

    # Set up logging configuration
    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.info("Logging initialized.")


"""
Logging helps track application behavior, diagnose issues, and improve
reliability by recording errors and key events, making debugging and
monitoring easier.

- The setup_logging function initializes logging if it is enabled
  in the configuration.
- The log_message function logs messages when logging is active.

Biblography
=============
Effective Logging in Python Applications.
https://realpython.com/python-logging/
"""
