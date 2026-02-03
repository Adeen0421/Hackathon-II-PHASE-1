from typing import List, Optional
from .models import Todo
from .storage import Storage

class TodoManager:
    def __init__(self, storage_file: str = "todos.json"):
        self.storage = Storage(storage_file)
        self.todos: List[Todo] = self.storage.load_todos()

    def add_todo(self, title: str, description: str = "") -> Todo:
        todo = Todo(title, description)
        self.todos.append(todo)
        self.storage.save_todos(self.todos)
        return todo

    def list_todos(self) -> List[Todo]:
        return self.todos

    def get_todo(self, todo_id: str) -> Optional[Todo]:
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def find_todo(self, identifier: str) -> Optional[Todo]:
        # Try by ID
        todo = self.get_todo(identifier)
        if todo:
            return todo
            
        # Try by Title (exact match)
        for todo in self.todos:
            if todo.title == identifier:
                return todo
        return None

    def complete_todo(self, identifier: str) -> bool:
        todo = self.find_todo(identifier)
        if todo:
            todo.completed = True
            self.storage.save_todos(self.todos)
            return True
        return False

    def delete_todo(self, identifier: str) -> bool:
        todo = self.find_todo(identifier)
        if todo:
            self.todos.remove(todo)
            self.storage.save_todos(self.todos)
            return True
        return False
