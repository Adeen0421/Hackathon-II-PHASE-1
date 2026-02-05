import sys
from .manager import TodoManager

class CLI:
    def __init__(self):
        self.manager = TodoManager()

    def print_help(self):
        print("\nAvailable commands:")
        print("  add               - Add a new todo")
        print("  list              - List all todos")
        print("  update <id|title> - Update a todo's details")
        print("  done <id|title>   - Mark a todo as completed by ID or Title")
        print("  delete <id|title> - Delete a todo by ID or Title")
        print("  exit              - Exit the application")

    def run(self):
        print("Welcome to the Todo CLI Application!")
        self.print_help()

        while True:
            try:
                command_input = input("\n> ").strip().split()
                if not command_input:
                    continue

                command = command_input[0].lower()
                args = command_input[1:]

                if command == "exit":
                    print("Goodbye!")
                    break
                elif command == "add":
                    self.handle_add()
                elif command == "list":
                    self.handle_list()
                elif command == "update":
                    if not args:
                        print("Error: Missing todo ID or Title. Usage: update <id|title>")
                    else:
                        self.handle_update(" ".join(args))
                elif command == "done":
                    if not args:
                        print("Error: Missing todo ID or Title. Usage: done <id|title>")
                    else:
                        self.handle_done(" ".join(args))
                elif command == "delete":
                    if not args:
                        print("Error: Missing todo ID or Title. Usage: delete <id|title>")
                    else:
                        self.handle_delete(" ".join(args))
                else:
                    print(f"Unknown command: {command}")
                    self.print_help()
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def handle_add(self):
        print("Enter todo details:")
        title = input("  Title: ").strip()
        while not title:
            print("  Title cannot be empty.")
            title = input("  Title: ").strip()
        
        description = input("  Description (optional): ").strip()
        todo = self.manager.add_todo(title, description)
        print(f"Todo added successfully! ID: {todo.id}")

    def handle_update(self, identifier: str):
        todo = self.manager.find_todo(identifier)
        if not todo:
            print(f"Error: Todo with ID or Title '{identifier}' not found.")
            return

        print(f"Updating todo '{todo.title}' (ID: {todo.id})")
        print("Leave fields blank to keep current values.")
        
        new_title = input(f"  Title [{todo.title}]: ").strip()
        new_description = input(f"  Description [{todo.description}]: ").strip()
        
        # Convert empty strings to None to indicate no change
        title_arg = new_title if new_title else None
        desc_arg = new_description if new_description else None
        
        if self.manager.update_todo(identifier, title_arg, desc_arg):
            print(f"Todo '{identifier}' updated successfully.")
        else:
            print(f"Error: Failed to update todo '{identifier}'.")

    def handle_list(self):
        todos = self.manager.list_todos()
        if not todos:
            print("No todos found.")
            return

        print("\nYour Todos:")
        print("-" * 60)
        for i, todo in enumerate(todos, 1):
            status = "✔" if todo.completed else "✖"
            print(f"{i}. [{status}] {todo.title} (ID: {todo.id})")
            if todo.description:
                print(f"       Desc: {todo.description}")
            print(f"       Created: {todo.created_at}")
        print("-" * 60)

    def handle_done(self, identifier: str):
        if self.manager.complete_todo(identifier):
            print(f"Todo '{identifier}' marked as completed.")
        else:
            print(f"Error: Todo with ID or Title '{identifier}' not found.")

    def handle_delete(self, identifier: str):
        if self.manager.delete_todo(identifier):
            print(f"Todo '{identifier}' deleted successfully.")
        else:
            print(f"Error: Todo with ID or Title '{identifier}' not found.")
