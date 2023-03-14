import psycopg2


def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost", database="PyCoders", user="postgres", password=123456
        )
        cur = conn.cursor()
        print("Connection Established")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    conn.autocommit = True

    try:
        queries = (
            """CREATE TABLE students(
                      student_id SERIAL PRIMARY KEY,
                      std_name VARCHAR(255) NOT NULL)""",
            """CREATE TABLE teachers(
                      teacher_id  SERIAL PRIMARY KEY,
                      teacher_name VARCHAR(255) NOT NULL)""",
        )
        for query in queries:
            cur.execute(query)
        print("Tables created")
    except:
        print("Table already exist")

    insert_queries = (
        """INSERT INTO students VALUES (1,'Ammar'),(2,'Esam'),(3,'Mohammed')""",
        """INSERT INTO teachers VALUES (1,'osama'),(2,'Fahd'),(3,'Ali')""",
    )
    for query in insert_queries:
        cur.execute(query)
        print("Data inserted")

    select_queries = ("""SELECT * from students""", """SELECT * from teachers""")
    for query in select_queries:
        cur.execute(query)
        print(cur.fetchall())


if __name__ == "__main__":
    connect()
