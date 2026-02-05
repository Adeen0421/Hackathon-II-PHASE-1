# Project Constitution

## 1. Core Principles
- **Spec-Driven Development**: All code must strictly follow the specifications in the `specs/` directory. No features shall be implemented unless explicitly specified.
- **Clean Architecture**: Maintain clear separation between CLI (presentation), Business Logic, and Data Storage layers.
- **Code Quality**: Code must be readable, well-structured, and follow standard Python conventions (PEP 8).
- **Simplicity**: Do not over-engineer. Use the simplest solution that satisfies the requirements.

## 2. Technical Constraints
- **Language**: Python 3.13+
- **UI**: Console/CLI only (No GUI, No Web).
- **Storage**: JSON file-based persistence (`todos.json`).
- **External Dependencies**: Minimized. Standard library preferred for core logic.

## 3. Workflow
1.  **Read Specs**: Always verify against `specs/` before implementation.
2.  **Plan**: Break down tasks based on requirements.
3.  **Implement**: Write clean, testable code.
4.  **Verify**: Ensure all features (Add, List, Update, Done, Delete) work as expected.

## 4. Forbidden Actions
- Do not manually edit logic without spec updates.
- Do not add features not in the specs ("Gold Plating").
- Do not use external databases (SQLite, Postgres, etc.) unless specified.
