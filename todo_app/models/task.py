"""
Task model for the Todo application
Defines the Task entity with id, title, description, and completion status
"""

class Task:
    """
    Represents a task in the todo list
    """

    def __init__(self, task_id, title, description="", completed=False):
        """
        Initialize a new task

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task (required)
            description (str): Optional description of the task
            completed (bool): Whether the task is completed (default: False)
        """
        self.id = task_id
        self.title = title.strip()
        self.description = description.strip()
        self.completed = completed

    def __str__(self):
        """
        String representation of the task
        """
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title}"

    def __repr__(self):
        """
        Representation of the task for debugging
        """
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"

    def to_dict(self):
        """
        Convert task to dictionary format
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    def mark_complete(self):
        """
        Mark the task as complete
        """
        self.completed = True

    def mark_incomplete(self):
        """
        Mark the task as incomplete
        """
        self.completed = False

    def update_title(self, new_title):
        """
        Update the task title

        Args:
            new_title (str): New title for the task
        """
        self.title = new_title.strip()

    def update_description(self, new_description):
        """
        Update the task description

        Args:
            new_description (str): New description for the task
        """
        self.description = new_description.strip()