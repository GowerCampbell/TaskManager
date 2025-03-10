# task manager/business_logic.py
import logging

from data_access import TaskRepository
from config import config
from models import Task


class TaskService:
    def __init__(self):
        """Initialise the TaskService with a TaskRepository."""
        self.task_repository = TaskRepository()
        self.task_max_length = config.get("task_max_length", 100)
        logging.info("TaskService initialized.")

    def get_all_tasks(self):
        """Get all tasks from the data source."""
        tasks = self.task_repository.get_tasks()
        logging.info(f"Retrieved {len(tasks)} tasks.")
        return tasks

    def add_task(self, title, description):
        """Add a new task to the data source."""
        if not title:
            logging.error("Task title cannot be empty.")
            raise ValueError("Task title cannot be empty.")
        if not description:
            logging.error("Task description cannot be empty.")
            raise ValueError("Task description cannot be empty.")
        if len(description) > self.task_max_length:
            logging.error(f"""
Description exceeds maximum length of {self.task_max_length} characters.""")
            raise ValueError(f"""
Description exceeds maximum length of {self.task_max_length} characters.""")
        task = Task(title, description)
        logging.debug(f"Task created: {task}")  # Debug log
        self.task_repository.save_task(task)
        logging.info(f"Added task: {task}")


"""
The business_logic.py module defines the TaskService class, which handles the
logic for managing tasks. It interacts with the TaskRepository to retrieve and
store task data while enforcing constraints like maximum task length. The
module also includes a Task class, representing individual tasks with a
title and description. This separation of concerns ensures a structured and
maintainable application design.

Biblography
============

Input Validation and Data Integrity in Python
https://realpython.com/python-data-validation/

"""
