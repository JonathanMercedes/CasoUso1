from sqlmodel import SQLModel, Session
from db.database import engine, create_db_and_tables, drop_db_and_tables
from models.todo_list import TodoList
from models.user import User
from models.task_status import TaskStatus
from models.task import Task
from auth.hashing import hash_password  # Importamos la función para hashear contraseñas

def seed_data():
    # Borrar la base de datos y las tablas existentes
    drop_db_and_tables() 
    # Crear la base de datos y las tablas
    create_db_and_tables()

    with Session(engine) as session:
        # Crear usuarios
        try:
            usuario1 = User(username="Lamine Yamal", email="LamineYamal@example.com", hashed_password=hash_password("password1"))
            usuario2 = User(username="Raphinha", email="Raphinha@example.com", hashed_password=hash_password("password2"))
            session.add_all([usuario1, usuario2])
            session.commit()
        except Exception as e:
            print(f"Error creating users: {e}")

        # Crear todo list
        try:
            list1 = TodoList(title="Lista1", owner_id=usuario1.id)
            list2 = TodoList(title="Lista2", owner_id=usuario2.id)
            session.add_all([list1, list2])
            session.commit()
        except Exception as e:
            print(f"Error creating lists: {e}")

        try:
            status1 = TaskStatus(name="Open")
            status2 = TaskStatus(name="InProgress")
            status3 = TaskStatus(name="Closed")
            session.add_all([status1, status2, status3])
            session.commit()
        except Exception as e:
            print(f"Error creating status: {e}")

        # Crear tasks
        try:
            task1 = Task(title="Task1", is_completed = False,todo_list_id = list1.id,status_id=status1.id)
            task2 = Task(title="Task2", is_completed = False,todo_list_id = list2.id,status_id=status2.id)
            session.add_all([task1, task2])
            session.commit()
        except Exception as e:
            print(f"Error creating tasks: {e}")

if __name__ == "__main__":
    seed_data()
