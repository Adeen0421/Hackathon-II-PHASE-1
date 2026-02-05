# Command Specs

## CLI Command Requirements
- `add` → prompts user for todo details
- `update <id>` → prompts user for new details (leave blank to keep current)
- `list` → displays all todos clearly
- `done <id|title>` → marks a todo as completed by ID or exact title
- `delete <id|title>` → deletes a todo by ID or exact title
- `exit` → safely exits the application

## Error Handling
- Handle invalid commands gracefully
- Handle non-existent todo IDs cleanly
- Never crash the application

## Output Requirements
- Generate all necessary Python files
- Ensure the app runs using: `python main.py`
- Print helpful messages for users
- Keep CLI UX simple and clean
