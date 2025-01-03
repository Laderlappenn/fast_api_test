import json

from sqlalchemy.orm import Session

from model.db_init import engine
from model.user import User
from error.exceptions import Missing, Duplicate



def get_all() -> list[User]:
    with Session(engine) as session:
        users = session.query(User).all()
        print(users)
    return users


def get_one(user_id: int) -> User:
    with Session(engine) as session:
        user = session.query(User).filter(User.id == user_id).first()
    return user


def create(user: User) -> User:
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)  # Refresh the user object to get the updated state (e.g., generated ID) # WHY??
    return user


def modify(user_id: int, user: User) -> User:
    with Session(engine) as session:
        db_user = session.get(User, user_id) # user.id
        if not db_user:
            raise Missing("User not found")

        # Update only the fields provided (partial update)
        for key, value in user.__dict__.items():
            if key != "_sa_instance_state" and value is not None:
                setattr(db_user, key, value)

        session.commit()
        session.refresh(db_user)
    return user


def replace(user_id: int, user: User) -> User:
    """
       Replace an entire user record in the database.
       """
    with Session(engine) as session:
        db_user = session.get(User, user_id) #user.id
        if not db_user:
            raise Missing("User not found")

        # Replace all fields with the new user's data
        for key, value in user.__dict__.items():
            if key != "_sa_instance_state":
                setattr(db_user, key, value)

        session.commit()
        session.refresh(db_user)
    return user


def delete(user_id: int) -> bool:
    """
       Delete a user record from the database.
       """
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if not db_user:
            raise Missing("User not found")
        session.delete(db_user)
        session.commit()
    return True # what to return???