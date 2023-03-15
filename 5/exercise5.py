import psycopg2
def connection():
    conn=None
    try:
        conn=psycopg2.connect(
            host="localhost",
            database="PyCoders",
            user="postgres",
            password="123321")
        conn.autocommit=True
        cur=conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS students
                    ( student_id SERIAL PRIMARY KEY,
                    student_name VARCHAR(255) NOT NULL
                    )
                    ''')
        cur.execute('''CREATE TABLE IF NOT EXISTS teachers
                    (teacher_id SERIAL PRIMARY KEY,
                    teacher_name VARCHAR(255) NOT NULL
                    )
                    ''')
        
        cur.execute('''INSERT INTO students(student_id,student_name) VALUES
                    (1, 'Yunus'),
                    (2,'Emre'),
                    (3,'Mehmet')
                    ON CONFLICT (student_id) DO NOTHING''')
        
        cur.execute('''INSERT INTO teachers(teacher_id,teacher_name) VALUES
                    (1,'Busra'),
                    (2,'Zehra'),
                    (3,'Tuba')
                    ON CONFLICT (teacher_id) DO NOTHING''')
        
        cur.execute('SELECT * FROM teachers')
        teachers_all=cur.fetchall()
        print(teachers_all)
        
        cur.execute('SELECT * FROM students')
        students_all=cur.fetchall()
        print(students_all)
        
    except(Exception,psycopg2.DatabaseError) as Error:
        print(Error)
    finally:
        if conn is not None:
            cur.close()
if __name__ == '__main__':
    connection()