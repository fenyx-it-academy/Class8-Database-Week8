import psycopg2
from config import *


try:

    # read connection parameters
    params = pycoders_db()

    # connect to the PostgreSQL server
    # print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)
    # create a cursor
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """)
    conn.commit()
    print("Created table students (if it does not already exist)!")

    cur.execute(
        "INSERT INTO students (name) VALUES ('Ramy'), ('Aaron'), ('Fenyx');")
    conn.commit()
    print("Added 3 sudents to the table.")

    # Create the teachers table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """)
    conn.commit()
    print("Created the table teachers (if it doesn't already exisit!)")

    # Insert 3 records into the teachers table
    cur.execute(
        "INSERT INTO teachers (name) VALUES ('Mr. Fenyxi'), ('Mr. Nerdi'), ('Mr. Geekie');")
    conn.commit()
    print("added 3 records into the teachers table.")

    print("All rows in the students table: ")
    cur.execute("SELECT * FROM public.students")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    print("All rows in the teachers table: ")
    cur.execute("SELECT * FROM public.teachers")
    rows = cur.fetchall()
    for row in rows:
        print(row)


except (Exception, psycopg2.Error) as error:
    print("error: ", error)

finally:
    # closing database connection.
    if conn:
        cur.close()
        conn.close()
        # print("PostgreSQL connection is closed")
