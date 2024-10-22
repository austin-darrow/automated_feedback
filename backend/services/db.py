import pyodbc
from sqlite3 import Connection

def get_db_connection():
    connection_str = (
        "DRIVER={PostgreSQL};"
        "DATABASE=mydatabase;"
        "UID=myuser;"
        "PWD=mypassword;"
        "SERVER=db;"
        "PORT=5432;"
    )
    conn = pyodbc.connect(connection_str)
    return conn


def get_db_cursor(db_connection):
    db_cursor = db_connection.cursor()
    return db_cursor

def create_user(email: str, password_hash: str, db_connection: Connection):
    db_cursor = get_db_cursor(db_connection)
    insert_query = f"""
    INSERT INTO users (email, password_hash)
    VALUES (?, ?);
    """
    db_cursor.execute(insert_query, [email, password_hash])
    db_connection.commit()
    db_cursor.close()

def insert_essay(essay: str, feedback: str, teacher_id: int, assignment_id: int, db_connection):
    db_cursor = get_db_cursor(db_connection)

    insert_query = """
    INSERT INTO essays (teacher_id, assignment_id, content, feedback)
    VALUES (?, ?, ?, ?);
    """

    # Pass the actual values as parameters
    db_cursor.execute(insert_query, (teacher_id, assignment_id, essay, feedback))

    db_connection.commit()
    db_cursor.close()

def get_essay(teacher_id: int, assignment_id: int, db_connection: Connection):
    db_cursor = get_db_cursor(db_connection)
    select_query = f"""
    SELECT content
    FROM essays
    WHERE teacher_id = {teacher_id} AND assignment_id = {assignment_id};
    """
    results = db_cursor.execute(select_query).fetchall()
    essays = []
    for row in results:
        essays.append(row.content)
    return essays

def create_assignment(title: str, teacher_id: int, db_connection: Connection):
    db_cursor = get_db_cursor(db_connection)
    insert_query = f"""
    INSERT INTO assignments (teacher_id, title)
    VALUES ({teacher_id}, '{title}');
    """
    db_cursor.execute(insert_query)
    db_connection.commit()
    db_cursor.close()