import psycopg2

conn = None

conn = psycopg2.connect(
    host = "localhost",
    database = "Pycoders",
    user = "postgres",
    password = "12345678"
)
conn.autocommit = True
cur = conn.cursor()


try:

    cur.execute("SELECT * FROM students;")
    students_information = cur.fetchall()
    print("**************student table************************")
    for student in students_information :
        print(student)

    cur.execute("SELECT * FROM teachers;")
    teacher_information = cur.fetchall()
    print("****************teachers table**********************")
    for teacher in teacher_information:
        print(teacher)
except : 
    cur.execute("CREATE TABLE students (student_id integer , name VARCHAR );")
    cur.execute("INSERT INTO students (student_id, name) values (1,'Mohammad');")
    cur.execute("INSERT INTO students (student_id, name) values (2,'Ahmad');")
    cur.execute("INSERT INTO students (student_id, name) values (3,'Yaser');")
    cur.execute("CREATE TABLE teachers (teacher_id integer , name VARCHAR );")
    cur.execute("INSERT INTO teachers (teacher_id, name) values (1,'Sara');")
    cur.execute("INSERT INTO teachers (teacher_id, name) values (2,'Sindy');")
    cur.execute("INSERT INTO teachers (teacher_id, name) values (3,'Sozan');")




conn.close()