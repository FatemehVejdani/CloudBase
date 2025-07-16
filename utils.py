
from models import db


def create_table(model):
    if db.is_closed():
        db.connect()

    try:
        db.create_tables([model], safe=True)
        print(f"Table for {model.__name__} created successfully.")
    except Exception as e:
        print(f"Error while creating table for {model.__name__}:", e)
    finally:
        if not db.is_closed():
            db.close()
