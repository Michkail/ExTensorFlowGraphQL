from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from .application import db
from models.sample_model import Todo


@convert_kwargs_to_snake_case
def resolve_create_todo(obj, info, description, due_date):
    try:
        due_date = datetime.strptime(due_date, '%d-%m-%Y').date()
        todo = Todo(id=2, completed=False, description=description, due_date=due_date)

        db.session.add(todo)
        db.session.commit()

        payload = {"success": True, "todo": todo.to_dict()}

    except ValueError:
        payload = {"success": False,
                   "errors": [f"Incorrect date format provided. Date should be in "
                              f"the format dd-mm-yyyy"]}

    return payload
