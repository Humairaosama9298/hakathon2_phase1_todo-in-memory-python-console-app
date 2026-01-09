---
description: "Task list for Todo In-Memory Python Console App implementation"
---

# Tasks: Todo In-Memory Python Console App

**Input**: Design documents from `/specs/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No explicit tests requested in feature specifications.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Project Structure**: `todo_app/` at repository root
- **Models**: `todo_app/models/`
- **Services**: `todo_app/services/`
- **CLI**: `todo_app/cli/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure with todo_app/ directory
- [x] T002 Create main.py entry point file
- [x] T003 [P] Create models/, services/, and cli/ directories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task model in todo_app/models/task.py
- [x] T005 Create TaskService in todo_app/services/task_service.py
- [x] T006 Create Menu class in todo_app/cli/menu.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with title and optional description to the in-memory list

**Independent Test**: User can start the application, select the add task option, enter a title and description, and see the task added with a unique ID and incomplete status

### Implementation for User Story 1

- [x] T007 [P] [US1] Implement Task class with id, title, description, and completed attributes in todo_app/models/task.py
- [x] T008 [US1] Implement TaskService.add_task() method in todo_app/services/task_service.py
- [x] T009 [US1] Implement add_task functionality in Menu class in todo_app/cli/menu.py
- [x] T010 [US1] Add input validation for empty titles in todo_app/services/task_service.py
- [x] T011 [US1] Update main.py to integrate add task functionality

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Tasks (Priority: P2)

**Goal**: Enable users to view all tasks with their ID, title, and completion status

**Independent Test**: User can start the application, select the view tasks option, and see all existing tasks with their details clearly displayed

### Implementation for User Story 2

- [x] T012 [P] [US2] Implement TaskService.get_all_tasks() method in todo_app/services/task_service.py
- [x] T013 [US2] Implement view_tasks functionality in Menu class in todo_app/cli/menu.py
- [x] T014 [US2] Add display formatting for tasks in todo_app/cli/menu.py
- [x] T015 [US2] Update main.py to integrate view tasks functionality
- [x] T016 [US2] Handle empty task list scenario in todo_app/cli/menu.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task (Priority: P3)

**Goal**: Enable users to update existing tasks by modifying title and/or description

**Independent Test**: User can start the application, select the update task option, enter a valid task ID, provide new title/description, and see the task updated

### Implementation for User Story 3

- [x] T017 [P] [US3] Implement TaskService.update_task() method in todo_app/services/task_service.py
- [x] T018 [US3] Implement update_task functionality in Menu class in todo_app/cli/menu.py
- [x] T019 [US3] Add validation for existing task ID in todo_app/services/task_service.py
- [x] T020 [US3] Update main.py to integrate update task functionality

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P4)

**Goal**: Enable users to delete existing tasks by their ID with confirmation

**Independent Test**: User can start the application, select the delete task option, enter a valid task ID, confirm deletion, and see the task removed

### Implementation for User Story 4

- [x] T021 [P] [US4] Implement TaskService.delete_task() method in todo_app/services/task_service.py
- [x] T022 [US4] Implement delete_task functionality in Menu class in todo_app/cli/menu.py
- [x] T023 [US4] Add confirmation prompt for deletion in todo_app/cli/menu.py
- [x] T024 [US4] Update main.py to integrate delete task functionality

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Task Complete/Incomplete (Priority: P5)

**Goal**: Enable users to change the completion status of existing tasks

**Independent Test**: User can start the application, select the mark task option, enter a valid task ID, choose completion status, and see the status updated

### Implementation for User Story 5

- [x] T025 [P] [US5] Implement TaskService.mark_task_completed() method in todo_app/services/task_service.py
- [x] T026 [US5] Implement mark_task_status functionality in Menu class in todo_app/cli/menu.py
- [x] T027 [US5] Add completion status toggle logic in todo_app/services/task_service.py
- [x] T028 [US5] Update main.py to integrate mark task functionality

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T029 [P] Add error handling for invalid user inputs across all CLI functions
- [x] T030 [P] Improve user interface formatting and messages
- [x] T031 Add graceful exit functionality to main.py
- [x] T032 Implement main menu loop with all options in main.py
- [x] T033 Run quickstart validation to ensure all features work correctly

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Models within a story marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement Task class with id, title, description, and completed attributes in todo_app/models/task.py"
Task: "Implement TaskService.add_task() method in todo_app/services/task_service.py"
Task: "Implement add_task functionality in Menu class in todo_app/cli/menu.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence