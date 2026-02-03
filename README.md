# Todo CLI Application (Phase 1)

This is a Python-based Todo CLI application built using Spec-Driven Development.

## Usage

To run the application:

```bash
python main.py
```

## Commands

- `add` - Add a new todo (prompts for title and description)
- `list` - List all todos with status
- `done <id>` - Mark a todo as completed
- `delete <id>` - Delete a todo
- `exit` - Exit the application

## Specifications

The project specifications are located in the `specs/` directory:
- `specs/todo.feature.md`: Functional requirements
- `specs/data.model.md`: Data and storage requirements
- `specs/commands.spec.md`: CLI command requirements

## Structure

- `main.py`: Entry point
- `todo_app/`: Application package
  - `cli.py`: CLI handling
  - `manager.py`: Business logic
  - `models.py`: Data models
  - `storage.py`: Persistence (JSON)
