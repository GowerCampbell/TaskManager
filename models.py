# taskmanager/models.py

class Task:
    def __init__(self, title, description):
        """Initialises a Task object with a title and description."""
        if not title:
            raise ValueError("Task title cannot be empty.")
        if not description:
            raise ValueError("Task description cannot be empty.")
        self.title = title
        self.description = description

    def __str__(self):
        """Return a string representation of the task."""
        return f"{self.title}: {self.description}"

"""
This task reinforced my understanding of OOP, validation, and error handling 
in Python. Ensuring required attributes and adding a __str__ method improved
 usability and data integrity.

Bibliography:
==============================
Python Software Foundation. Classes and Object-Oriented Programming.
https://docs.python.org/3/tutorial/classes.html
"""
