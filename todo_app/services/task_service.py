"""
Task service for the Todo application
Handles business logic for task operations
"""

from ..models.task import Task


class TaskService:
    """
    Service class to handle task operations
    Manages the in-memory storage of tasks
    """

    def __init__(self):
        """
        Initialize the task service with an empty task list
        """
        self._tasks = {}
        self._next_id = 1

    def add_task(self, title, description=""):
        """
        Add a new task to the list

        Args:
            title (str): Title of the task (required)
            description (str): Optional description of the task

        Returns:
            Task: The created task object

        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        # Validate title
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        # Create new task with the next available ID
        task = Task(self._next_id, title, description, False)
        self._tasks[self._next_id] = task

        # Increment the next ID for the subsequent task
        self._next_id += 1

        return task

    def get_task_by_id(self, task_id):
        """
        Get a task by its ID

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Task: The task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self):
        """
        Get all tasks

        Returns:
            list: List of all task objects
        """
        return list(self._tasks.values())

    def update_task(self, task_id, new_title=None, new_description=None):
        """
        Update an existing task

        Args:
            task_id (int): ID of the task to update
            new_title (str, optional): New title for the task
            new_description (str, optional): New description for the task

        Returns:
            Task: The updated task object

        Raises:
            KeyError: If the task with the given ID doesn't exist
            ValueError: If new_title is empty or contains only whitespace
        """
        task = self.get_task_by_id(task_id)
        if not task:
            raise KeyError(f"Task with ID {task_id} does not exist")

        # Update title if provided
        if new_title is not None:
            if not new_title.strip():
                raise ValueError("Task title cannot be empty or contain only whitespace")
            task.update_title(new_title)

        # Update description if provided
        if new_description is not None:
            task.update_description(new_description)

        return task

    def delete_task(self, task_id):
        """
        Delete a task by its ID

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if it didn't exist
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def mark_task_completed(self, task_id, completed=True):
        """
        Mark a task as completed or incomplete

        Args:
            task_id (int): ID of the task to update
            completed (bool): Whether the task should be marked as completed

        Returns:
            Task: The updated task object

        Raises:
            KeyError: If the task with the given ID doesn't exist
        """
        task = self.get_task_by_id(task_id)
        if not task:
            raise KeyError(f"Task with ID {task_id} does not exist")

        if completed:
            task.mark_complete()
        else:
            task.mark_incomplete()

        return task

    def get_next_id(self):
        """
        Get the next available ID for a new task

        Returns:
            int: The next available task ID
        """
        return self._next_id

    def get_task_count(self):
        """
        Get the total number of tasks

        Returns:
            int: The number of tasks in the service
        """
        return len(self._tasks)