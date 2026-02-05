# Todo Feature Specs

## Functional Requirements
- Users can add a todo
- Users can list all todos
- Users can update a todo's details (title, description)
- Users can mark a todo as completed (by ID or Title)
- Users can delete a todo (by ID or Title)
- Todos must persist between program runs

## Architecture Requirements
- Separate concerns clearly:
  - CLI handling
  - Business logic
  - Data storage
- Use readable function and file naming
- Keep the project simple and understandable

## Bonus Requirements
- Todos should be displayed in a user-friendly numbered list with status indicators (✔ / ✖).
