import uuid
from datetime import datetime
from typing import Optional, Dict, Any

class Todo:
    def __init__(self, title: str, description: str = "", completed: bool = False, 
                 created_at: Optional[str] = None, todo_id: Optional[str] = None):
        self.id = todo_id if todo_id else str(uuid.uuid4())
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at if created_at else datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Todo':
        return cls(
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
            created_at=data.get("created_at"),
            todo_id=data.get("id")
        )
