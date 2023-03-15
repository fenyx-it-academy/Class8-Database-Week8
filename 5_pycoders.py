import psycopg2

def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host="localhost",
            database="PyCoders",
            user="postgres",
            password="data")

        conn.autocommit = True 
        curr = conn.cursor()
        curr.execute("""CREATE TABLE students (
            student_id bigint,
            name text
        );""")

        curr.execute("""CREATE TABLE teachers (
            teacher_id bigint,
            name text
        );""")


        curr.execute("""INSERT INTO teachers 
        
        VALUES 
        (
           1,
           'Vasiliy Petrov'
        ),
        (
           2,
           'Michail Chekhov'
        ),
        (
           3,
           'Platon Petrov'
        )
        """)

        curr.execute("""INSERT INTO students 
        
        VALUES 
        (
           176,
           'Danila Veter'
        ),
        (
           252,
           'Ann White'
        ),
        (
           383,
           'John Smith'
        )
        """)

        curr.execute("SELECT * FROM students")
        students = curr.fetchall()
        print ()
        print ("All students this BD:")
        for student in students:
            print(student)

        curr.execute("SELECT * FROM teachers")
        teachers = curr.fetchall()
        print ()
        print ("All teachers this DB:")
        for teacher in teachers:
            print(teacher)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)      
    finally: 
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()