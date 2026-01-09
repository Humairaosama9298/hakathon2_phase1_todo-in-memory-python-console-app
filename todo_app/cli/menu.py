"""
Menu class for the Todo application
Handles the CLI interface and user interactions
"""

from todo_app.services.task_service import TaskService


class Menu:
    """
    Menu class to handle CLI interactions
    Provides the interface for users to interact with the task service
    """

    def __init__(self):
        """
        Initialize the menu with a task service
        """
        self.task_service = TaskService()
        self.running = True

    def display_menu(self):
        """
        Display the main menu options
        """
        print("\n" + "="*40)
        print("TODO APPLICATION MENU")
        print("="*40)
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as complete/incomplete")
        print("6. Exit")
        print("="*40)

    def get_user_choice(self):
        """
        Get the user's menu choice

        Returns:
            str: The user's choice
        """
        try:
            choice = input("Enter your choice (1-6): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\n\nOperation cancelled by user.")
            return "6"  # Return exit choice

    def handle_add_task(self):
        """
        Handle the add task functionality
        """
        print("\n--- ADD TASK ---")
        try:
            title = input("Enter task title: ").strip()

            # Check if title is empty
            if not title:
                print("Error: Task title cannot be empty.")
                return

            description = input("Enter task description (optional): ").strip()

            task = self.task_service.add_task(title, description)
            print(f"\nTask added successfully!")
            print(f"ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Status: {'Completed' if task.completed else 'Incomplete'}")

        except ValueError as e:
            print(f"\nError: {e}")

    def handle_view_tasks(self):
        """
        Handle the view tasks functionality
        """
        print("\n--- VIEW ALL TASKS ---")

        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        print(f"\nTotal tasks: {len(tasks)}")
        print("-" * 50)

        for task in tasks:
            status = "✓ Completed" if task.completed else "○ Incomplete"
            print(f"ID: {task.id} | {status} | Title: {task.title}")
            if task.description:
                print(f"     Description: {task.description}")
            print("-" * 50)

    def handle_update_task(self):
        """
        Handle the update task functionality
        """
        print("\n--- UPDATE TASK ---")

        try:
            task_id_input = input("Enter task ID to update: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return

        # Check if task exists
        existing_task = self.task_service.get_task_by_id(task_id)
        if not existing_task:
            print(f"Error: Task with ID {task_id} does not exist.")
            return

        print(f"Current task: {existing_task}")
        print(f"Current description: {existing_task.description}")

        # Get new title (or keep current if empty)
        new_title_input = input(f"Enter new title (leave empty to keep '{existing_task.title}'): ").strip()
        new_title = new_title_input if new_title_input else None

        # Get new description (or keep current if empty)
        new_description_input = input(f"Enter new description (leave empty to keep current): ").strip()
        new_description = new_description_input if new_description_input != "" else None

        try:
            updated_task = self.task_service.update_task(task_id, new_title, new_description)
            print(f"\nTask updated successfully!")
            print(f"ID: {updated_task.id}")
            print(f"Title: {updated_task.title}")
            print(f"Description: {updated_task.description}")
            print(f"Status: {'Completed' if updated_task.completed else 'Incomplete'}")

        except ValueError as e:
            print(f"\nError: {e}")

    def handle_delete_task(self):
        """
        Handle the delete task functionality
        """
        print("\n--- DELETE TASK ---")

        try:
            task_id_input = input("Enter task ID to delete: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return

        # Check if task exists and show details before deletion
        existing_task = self.task_service.get_task_by_id(task_id)
        if not existing_task:
            print(f"Error: Task with ID {task_id} does not exist.")
            return

        print(f"Task to delete: {existing_task}")
        if existing_task.description:
            print(f"Description: {existing_task.description}")

        # Confirm deletion
        confirm = input(f"\nAre you sure you want to delete task {task_id}? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("Task deletion cancelled.")
            return

        # Perform deletion
        success = self.task_service.delete_task(task_id)
        if success:
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"Failed to delete task with ID {task_id}.")

    def handle_mark_task_status(self):
        """
        Handle the mark task status functionality
        """
        print("\n--- MARK TASK STATUS ---")

        try:
            task_id_input = input("Enter task ID: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return

        # Check if task exists
        existing_task = self.task_service.get_task_by_id(task_id)
        if not existing_task:
            print(f"Error: Task with ID {task_id} does not exist.")
            return

        print(f"Current task: {existing_task}")

        # Get status choice
        status_choice = input("Mark as (c)omplete or (i)ncomplete? (c/i): ").strip().lower()

        if status_choice in ['c', 'complete']:
            completed = True
            status_str = "completed"
        elif status_choice in ['i', 'incomplete']:
            completed = False
            status_str = "incomplete"
        else:
            print("Invalid choice. Please enter 'c' for complete or 'i' for incomplete.")
            return

        try:
            updated_task = self.task_service.mark_task_completed(task_id, completed)
            print(f"\nTask marked as {status_str} successfully!")
            print(f"ID: {updated_task.id}")
            print(f"Title: {updated_task.title}")
            print(f"Status: {'Completed' if updated_task.completed else 'Incomplete'}")

        except KeyError as e:
            print(f"\nError: {e}")

    def handle_exit(self):
        """
        Handle the exit functionality
        """
        print("\nThank you for using the Todo Console App!")
        print("Goodbye!")
        self.running = False

    def run(self):
        """
        Run the main menu loop
        """
        print("Welcome to the Todo Console App!")

        while self.running:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.handle_add_task()
            elif choice == "2":
                self.handle_view_tasks()
            elif choice == "3":
                self.handle_update_task()
            elif choice == "4":
                self.handle_delete_task()
            elif choice == "5":
                self.handle_mark_task_status()
            elif choice == "6":
                self.handle_exit()
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.")