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
    db_cursor.execute('SET NOCOUNT ON;')
    return db_cursor

def insert_essay(essay: str, teacher_id: int, assignment_id: int, db_connection: Connection):
    db_cursor = get_db_cursor(db_connection)
    insert_query = f"""
    INSERT INTO essays (teacher_id, assignment_id, content)
    VALUES ({teacher_id}, {assignment_id}, '{essay}');
    """
    db_cursor.execute(insert_query)
    db_connection.commit()
    db_cursor.close()
