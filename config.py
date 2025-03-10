# taskmanager/config.py

import json


class Config:
    def __init__(self, config_file="config.json"):
        with open(config_file, "r") as file:
            self.settings = json.load(file)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def get_logging_config(self):
        """Get logging configuration from the settings."""
        return self.settings.get("logging", {})


# Global configuration object
config = Config()

# Global configuration object
config = Config()

"""
This module manages the configuration settings for the application. It defines
the Config class, which loads settings from a JSON file and provides a method
to retrieve these values. In a real-world application, this module could be
expanded to include settings for database connections, logging, and other
configurable parameters.

Bibliography
============
Python Software Foundation. json.
https://docs.python.org/3/library/json.html

JSON for Configuration Storage
https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON

"""
