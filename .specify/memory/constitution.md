# Todo Phase 1 – Project Constitution

## Project Vision
This project is a Phase 1 implementation of the "Evolution of Todo" hackathon.
The goal is to build a clean, reliable, in-memory Python console-based Todo
application using Spec-Driven Development with Claude Code and Spec-Kit Plus.

The developer must act as a system architect, not a manual coder.

## Core Principles
- No manual code writing is allowed
- All code must be generated via Claude Code
- Specs are the single source of truth
- Code quality matters more than speed
- Simplicity over complexity

## Technical Constraints
- Language: Python 3.13+
- Runtime: Console / CLI only
- Storage: In-memory only (no database, no files)
- External libraries are NOT allowed
- Application must run via terminal

## Architectural Rules
- Code must be modular and readable
- Use classes for core domain logic
- Separate concerns (models, services, CLI)
- Each task must have a unique numeric ID
- State must persist only during runtime

## Functional Scope (Phase 1 Only)
The application must support exactly the following features:
1. Add a task
2. View all tasks
3. Update a task
4. Delete a task
5. Mark task as complete or incomplete

No extra features are allowed in Phase 1.

## CLI Behavior Rules
- Application must show a menu repeatedly until exit
- User input errors must be handled gracefully
- Clear messages must be shown for success/failure
- Tasks must display completion status clearly

## Spec Compliance
- Every feature must be backed by a specification file
- Claude Code must strictly follow specs
- If output is incorrect, specs must be refined
- Specs take priority over implementation details

## Definition of Done
Phase 1 is complete only if:
- All 5 required features work correctly
- Application runs without errors
- Code structure follows the constitution
- Specs and implementation are aligned

## Governance
- This constitution supersedes all other practices
- Amendments require documentation, approval, and migration plan
- All PRs/reviews must verify compliance with these principles
- Complexity must be justified with clear benefits

**Version**: 1.0.0 | **Ratified**: 2026-01-09 | **Last Amended**: 2026-01-09
