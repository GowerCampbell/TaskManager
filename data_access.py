# TaskManager/data_access.py
import os
import json
import logging
from config import config
from models import Task


class TaskRepository:
    def __init__(self):
        self.data_folder = config.get("data_folder", "tasks_data")
        self.filename = os.path.join(
            self.data_folder, config.get("data_file", "tasks.json"))
        self._ensure_data_folder_exists()

    def _ensure_data_folder_exists(self):
        """Create the data folder if it doesn't exist."""
        try:
            if not os.path.exists(self.data_folder):
                os.makedirs(self.data_folder)
                logging.info(f"Created data folder: {self.data_folder}")
        except OSError as e:
            logging.error(f"Error creating data folder: {e}")
            raise

    def get_tasks(self):
        """Retrieve tasks from the data source."""
        try:
            with open(self.filename, "r") as file:
                task_list = json.load(file)  # Load the entire file as a JSON list
                tasks = [Task(task["title"], task["description"]) 
                         for task in task_list]
                logging.debug(f"Tasks retrieved: {task_list}")  # Debug log
                logging.info(f"Retrieved {len(tasks)} tasks from {self.filename}")
                return tasks
        except FileNotFoundError:
            logging.warning(f"File not found: {self.filename}. Starting fresh.")
            return []
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from {self.filename}: {e}")
            return []
        except KeyError as e:
            logging.error(f"Invalid task data in {self.filename}: missing {e}")
            return []

    def save_task(self, task):
        """Save a task to the data sink."""
        # Load existing tasks
        tasks = self.get_tasks()  # Reuse get_tasks to handle file reading
        task_data = {"title": task.title, "description": task.description}
        
        # Append the new task
        tasks.append(task)
        
        try:
            with open(self.filename, "w") as file:
                # Write the entire list back as JSON
                json.dump([{"title": t.title, "description": t.description} 
                           for t in tasks], file, indent=4)
                logging.debug(f"Task saved to file: {task_data}")  # Debug log
                logging.info(f"Saved task: {task}")
        except IOError as e:
            logging.error(f"Error saving task to {self.filename}: {e}")
            raise


"""
(Thanks you for the assist!!!)

The data_access.py module, which manages the storage and retrieval of tasks now 
reads a the entire file as a single JSON list [{"title": "Task 1", "description":
 "Desc 1"}, ...]) while the save_task() loads the existing tasks appends the new
task and writes the updtaed list to the json file definesd in the TaskRepository 
class in a data folder, which handles reading the tasks from and saving tasks 
to a file. The module ensures the necessary data folder then exists, which I 
learned from performing operations for file paths. It includes some error 
handling to address issues like missing files or permission errors when 
the application runs.

Bibliography:
==============================
Python Software Foundation.
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

Python Software Foundation. os
https://docs.python.org/3/library/os.html
"""
