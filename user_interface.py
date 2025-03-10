# task manager/user_interface.py

import os
import logging
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from business_logic import TaskService


# Initialize Rich console
console = Console()


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def display_tasks(task_service):
    """Display tasks in a formatted table."""
    tasks = task_service.get_all_tasks()
    logging.debug(f"Tasks retrieved for display: {tasks}")  # Debug log
    if not tasks:
        console.print("\n[bold yellow]No tasks found![/bold yellow]")
        logging.info("No tasks found.")
        return

    table = Table(title="Tasks", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=12)
    table.add_column("Title")
    table.add_column("Description")

    for idx, task in enumerate(tasks, start=1):
        title = getattr(task, 'title', 'No Title')
        description = getattr(task, 'description', 'No Description')
        table.add_row(str(idx), title, description)
        logging.debug(
            f"Task added to table: {title} - {description}")
    console.print(table)
    logging.info("Displayed tasks.")


def add_task(task_service):
    """Prompt the user to add a new task."""
    title = Prompt.ask("\nEnter Task Title:")
    description = Prompt.ask("Enter Task Description:")
    try:
        task_service.add_task(title, description)
        console.print("[bold green]Task added successfully![/bold green]")
        logging.info(f"User added task: {title} - {description}")
    except ValueError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        logging.error(f"Error adding task: {e}")


def show_menu():
    """Display the main menu."""
    console.print(Panel("Task Management Application", style="bold blue"))
    console.print("\n==================================", style="bold blue")
    console.print("Menu:", style="bold blue")
    console.print("1. View Tasks")
    console.print("2. Add Task")
    console.print("3. Quit")


def start_taskmanager():
    """Starts the Task Management Application."""
    logging.info("Task Manager application started.")
    task_service = TaskService()
    while True:
        clear_screen()  # Clears the screen before showing the menu
        show_menu()
        choice = IntPrompt.ask("""
\nEnter your choice", choices=["1", "2", "3"]""")

        if choice == 1:
            clear_screen()
            display_tasks(task_service)
            console.input("""
\nPress [bold]Enter[/bold] to return to the menu...""")
        elif choice == 2:
            clear_screen()
            add_task(task_service)
            console.input("""
\nPress [bold]Enter[/bold] to return to the menu...""")
        elif choice == 3:
            console.print("""
[bold magenta]Exiting the application. Goodbye![/bold magenta]""")
            logging.info("User exited the application.")
            break
        else:
            console.print("""
bold red]Invalid choice. Please try again.[/bold red]""")
            logging.warning("""
User entered an invalid choice.""")
            console.input("""
\nPress [bold]Enter[/bold] to continue...""")


"""
This module handles the user interface logic for the application using
the rich library for enhanced terminal output. I learned it provides functions
that can  display tasks in a formatted table, adding new tasks via user input,
and to navigate a simple command-line menu. The start_taskmanager function
initializes the TaskService and manages user interactions, allowing users to
view, add tasks, and (optionally) access logs.

Bibliography
==============

Rich Library Documentation
https://rich.readthedocs.io

Python Official Documentation
https://docs.python.org/3/

Operating System Module
https://docs.python.org/3/library/os.html

"""
