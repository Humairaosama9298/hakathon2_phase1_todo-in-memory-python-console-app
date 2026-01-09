# Mark Task Complete/Incomplete Specification

## Feature Description
Functionality to change the completion status of existing tasks in the in-memory todo list, allowing users to mark tasks as complete or incomplete as they progress.

## User Scenarios & Testing
- As a user, I want to mark a task as complete so that I can track my progress
- As a user, I want to mark a completed task as incomplete if I need to revisit it
- As a user, I want to select a task by its ID to change its status so that I can modify the correct task
- As a user, I want to be notified if I enter an invalid task ID so that I can correct my input
- As a user, I want to see the updated status after changing it so that I can confirm the change
- As a user, I want to choose whether to mark the task as complete or incomplete
- As a user, I want to return to the main menu after changing a task's status

## Functional Requirements
1. **Task Selection Process**
   - Prompt user for the task ID to modify
   - Validate that the provided task ID exists in the task list
   - Display the current status of the selected task
   - Display an error message if the task ID does not exist
   - Allow user to retry entering the task ID if invalid

2. **Status Change Process**
   - Present options to mark the task as complete or incomplete
   - Allow user to select the desired completion status
   - Update only the completion status of the selected task
   - Preserve all other task properties (ID, title, description)

3. **Input Validation**
   - Validate that the provided task ID exists in the task list
   - Validate that the user selection for status change is valid
   - Display error messages for invalid inputs
   - Allow user to retry after invalid input

4. **Data Handling**
   - Locate the task in the in-memory collection using the provided ID
   - Update only the completion status field of the existing task
   - Maintain the integrity of the task list structure
   - Preserve all other task properties during the update

5. **User Feedback**
   - Display the current status of the task before changing it
   - Display a success message after updating the status
   - Show the updated task details (ID, title, and new completion status)
   - Return to the main menu after successful status change

6. **Error Handling**
   - Handle invalid task IDs gracefully
   - Handle invalid status change selections appropriately
   - Allow user to cancel the operation if needed
   - Maintain data integrity if the status change fails

## Success Criteria
- Users can successfully change task completion status
- Task IDs, titles, and descriptions remain unchanged during status updates
- Updated completion status is reflected accurately in the task list
- Users receive clear feedback about status changes
- Users receive clear error messages when entering invalid task IDs
- Users can change tasks from complete to incomplete and vice versa
- The application handles all edge cases appropriately
- User can return to main menu after status change or cancellation

## Key Entities
- **Task Selector**: Component to locate and validate the task to modify
- **Status Changer**: Logic to update the completion status
- **Status Validator**: Logic to validate status change requests
- **Task Status Updater**: Service that modifies task completion status

## Dependencies
- Core task entity definition from 01-todo-core.spec.md
- In-memory storage system from core specification
- Menu navigation system from core specification

## Assumptions
- Users will know the ID of the task whose status they wish to change
- Users will understand the difference between complete and incomplete status
- The task list structure remains intact during status changes
- Users will use this feature to accurately track their task completion