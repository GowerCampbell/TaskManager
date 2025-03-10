
"""
# Modules Task 18: Task Manager
# Written by: GowerCambell
"""

from user_interface import start_taskmanager
from utilities import setup_logging

if __name__ == "__main__":
    setup_logging()
    start_taskmanager()

"""
This script acts as the main entry point for the Task Manager application.
It initializes logging (if enabled) using setup_logging() from the utilities
module and starts the user interface with start_taskmanager() from the user
_interface module. The if __name__ == "__main__": condition ensures the script
 runs only when executed directly, preventing unintended execution when
 imported as a module.


Bibliography
=============

Effective Logging in Python Applications
https://realpython.com/python-logging/

Input Validation and Data Integrity in Python
https://realpython.com/python-data-validation/

JSON for Configuration Storage
https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON

Operating System Module
https://docs.python.org/3/library/os.html

PEP 8 Style Guide for Python Code
https://peps.python.org/pep-0008/#constants

Python Official Documentation
https://docs.python.org/3/

Python Software Foundation - Input and Output
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

Python Software Foundation - JSON
https://docs.python.org/3/library/json.html

Python Software Foundation - Logging
https://docs.python.org/3/library/logging.html

Python Software Foundation - OS Module
https://docs.python.org/3/library/os.html

Rich Library Documentation
https://rich.readthedocs.io


"""
