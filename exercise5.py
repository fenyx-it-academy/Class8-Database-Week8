import psycopg2
def connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "PyCoders",
            user = "postgres",
            password = "Fenyx")
        conn.autocommit = True
        cur = conn.cursor()
        # cur.execute('''CREATE TABLE students 
        #             ( student_id SERIAL PRIMARY KEY, 
        #             name VARCHAR(255) NOT NULL)''')
        # cur.execute('''CREATE TABLE teachers
        #             ( teacher_id SERIAL PRIMARY KEY, 
        #             name VARCHAR(255) NOT NULL)''')
        cur.execute('''INSERT INTO students
                     ( student_id, name ) VALUES(1,'Ali'),(2,'Girmay'),(3,'Selam')''')
        
        cur.execute('''INSERT INTO teachers
                     ( teacher_id, name ) VALUES(1,'Haftom'),(2,'Dave'),(3,'Solomon')''')
        cur.execute('SELECT * FROM students')
        students_all = cur.fetchall()
        print(students_all)
       
        cur.execute('SELECT * FROM teachers')
        teachers_all = cur.fetchall()
        print(teachers_all)

    except(Exception,psycopg2.DatabaseError) as Error:
        print(Error)
    finally:
        if conn is not None:
            cur.close()
if __name__ == '__main__':
    connection()
