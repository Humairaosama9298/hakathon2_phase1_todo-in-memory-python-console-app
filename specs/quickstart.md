# Quickstart: Todo In-Memory Python Console App

## Running the Application

1. Ensure Python 3.13+ is installed on your system
2. Navigate to the project directory
3. Run the application:
   ```bash
   python todo_app/main.py
   ```

## Using the Application

1. The application will display a main menu with numbered options
2. Enter the number corresponding to the operation you want to perform:
   - 1: Add a new task
   - 2: View all tasks
   - 3: Update an existing task
   - 4: Delete a task
   - 5: Mark task as complete/incomplete
   - 6: Exit the application

3. Follow the prompts for each operation:
   - For adding tasks: Enter the task title and optional description
   - For viewing tasks: All tasks will be displayed with ID, title, and status
   - For updating tasks: Enter the task ID, then provide new title/description
   - For deleting tasks: Enter the task ID and confirm deletion
   - For marking tasks: Enter the task ID and select completion status

## Important Notes

- All data is stored in memory only and will be lost when the application exits
- Task IDs are assigned sequentially starting from 1
- The application validates inputs and provides error messages for invalid entries
- Use option 6 to exit the application cleanly