# Data Model: Todo In-Memory Python Console App

## Task Entity

### Fields
- **id** (int): Unique sequential identifier assigned when task is created
- **title** (str): Required text title of the task (non-empty after trimming whitespace)
- **description** (str): Optional text description of the task (can be empty)
- **completed** (bool): Boolean indicating completion status (default: False)

### Validation Rules
- id: Must be a positive integer, assigned sequentially starting from 1
- title: Must not be empty or contain only whitespace after trimming
- description: Can be empty or contain any text
- completed: Must be boolean value (True/False)

### State Transitions
- New task: completed = False (default)
- Mark complete: completed = True
- Mark incomplete: completed = False

## Task Collection

### Structure
- **tasks** (list/dict): In-memory collection storing Task entities
- Tasks accessible by ID for O(1) retrieval in dictionary implementation
- Maintains insertion order in list implementation

### Operations
- Add: Insert new Task with next sequential ID
- Get: Retrieve Task by ID
- Update: Modify Task fields by ID
- Delete: Remove Task by ID
- List: Retrieve all Tasks
- Find by completion status: Retrieve Tasks filtered by completion status

## Data Integrity
- Unique ID constraint: Each Task must have a unique ID
- Referential integrity: Operations target existing Task IDs only
- Validation: All field validations applied during create/update operations