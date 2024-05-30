from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from .application import db
from models.sample_model import SCM


@convert_kwargs_to_snake_case
def resolve_create_scm(obj, info, description, due_date):
    try:
        due_date = datetime.strptime(due_date, '%d-%m-%Y').date()
        scm = SCM(id=2, completed=False, description=description, due_date=due_date)

        db.session.add(scm)
        db.session.commit()

        payload = {"success": True, "scm": scm.to_dict()}

    except ValueError:
        payload = {"success": False,
                   "errors": [f"Incorrect date format provided. Date should be in "
                              f"the format dd-mm-yyyy"]}

    return payload
