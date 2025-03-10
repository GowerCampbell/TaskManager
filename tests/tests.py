# taskmanager/tests/tests.py

import unittest
import os
from business_logic import TaskService
from constants import TASK_MAX_LENGTH
from config import config


class TestTaskService(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.task_service = TaskService()
        # Ensure the data file is clean before each test
        self.data_file = config.get("data_file", "data.txt")
        if os.path.exists(self.data_file):
            os.remove(self.data_file)

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.data_file):
            os.remove(self.data_file)

    def test_add_task(self):
        """Test adding a valid task."""
        initial_task_count = len(self.task_service.get_all_tasks())
        self.task_service.add_task("Valid Task")
        updated_task_count = len(self.task_service.get_all_tasks())
        self.assertEqual(updated_task_count, initial_task_count + 1)

    def test_add_task_exceeds_max_length(self):
        """Test adding a task that exceeds the maximum length."""
        long_task = "a" * (TASK_MAX_LENGTH + 1)
        with self.assertRaises(ValueError):
            self.task_service.add_task(long_task)

    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        self.task_service.add_task("Task 1")
        self.task_service.add_task("Task 2")
        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn("Task 1", tasks)
        self.assertIn("Task 2", tasks)

    def test_add_empty_task(self):
        """Test adding an empty task."""
        with self.assertRaises(ValueError):
            self.task_service.add_task("")

    def test_add_duplicate_task(self):
        """Test adding a duplicate task."""
        self.task_service.add_task("Duplicate Task")
        initial_task_count = len(self.task_service.get_all_tasks())
        self.task_service.add_task("Duplicate Task")  # Add the same task again
        updated_task_count = len(self.task_service.get_all_tasks())
        self.assertEqual(updated_task_count, initial_task_count + 1)

    def test_get_all_tasks_empty(self):
        """Test retrieving tasks when no tasks are present."""
        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_task_persistence(self):
        """Test that tasks are persisted across service instances."""
        self.task_service.add_task("Persisted Task")
        # Creates a new instance of TaskService
        new_task_service = TaskService()
        tasks = new_task_service.get_all_tasks()
        self.assertIn("Persisted Task", tasks)


if __name__ == "__main__":
    unittest.main()

"""
The script contains my unit tests for the TaskService class, focusing on
improvements like test independence, additional test cases, dynamic
configuration, and error handling.

I learned that Test independence ensures that each test runs in isolation.
This setUp method deletes the data file (data.txt) before each test, and
the tearDown method cleans up afterward, preventing any test from affecting
another.

The script adds new test cases to check for various scenarios: adding empty
tasks, handling duplicate tasks, behavior when no tasks are present, and
ensuring task persistence across different instances of TaskService.

The tests now use a configuration from javascript to retrieve the data file
path from a configuration module, making them more flexible. Error handling
is improved with checks for edge cases, like empty tasks and task persistence.

To run the tests, use:

python3 -m unittest taskmanager/tests/tests.py.

If all tests pass, you'll see a confirmation that 7 tests ran successfully.

Bibliography:

Python Documentation. "Unit testing framework."
 https://docs.python.org/3/library/unittest.html


"""
