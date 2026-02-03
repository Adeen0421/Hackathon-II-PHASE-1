import json
import os
from typing import List, Dict, Any
from .models import Todo

class Storage:
    def __init__(self, filename: str = "todos.json"):
        self.filename = filename

    def load_todos(self) -> List[Todo]:
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Todo.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError):
            return []

    def save_todos(self, todos: List[Todo]) -> None:
        data = [todo.to_dict() for todo in todos]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
