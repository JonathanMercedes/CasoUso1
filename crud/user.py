from sqlmodel import Session, select
from models.user import User

def get_users(session: Session):
    return session.exec(select(User)).all()
