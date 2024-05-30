import uuid

from main import db


class SCM(db.Model):
    id = db.Column(db.String(36), default=lambda: str(uuid.uuid4()), primary_key=True, unique=True)
    description = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "completed": self.completed,
            "description": self.description,
            "due_date": str(self.due_date.strftime('%d-%m-%Y'))
        }
