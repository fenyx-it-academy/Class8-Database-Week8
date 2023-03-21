import psycopg2

def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        try:
            # try to connect to database
            conn = psycopg2.connect(
                host="localhost",
                database="Pycoders",
                user="postgres",
                password="1")
        except (Exception, psycopg2.DatabaseError) as error:
            pass
       

        conn.autocommit = True # this command enables autocommit to postgreSQL otherwise at the end of each operation you must do conn.commit()
      
  
        curr = conn.cursor()
        curr.execute("CREATE TABLE students (student_id integer , student_name VARCHAR );")
        curr.execute("CREATE TABLE teachers (teacher_id integer , teacher_name VARCHAR );")

        curr.execute("INSERT INTO students (student_id, student_name) values (1,'bahadir');")
        curr.execute("INSERT INTO students (student_id, student_name) values (2,'ceren');")
        curr.execute("INSERT INTO students (student_id, student_name) values (3,'talha');")
       
        curr.execute("INSERT INTO teachers (teacher_id, teacher_name) values (1,'elon');")
        curr.execute("INSERT INTO teachers (teacher_id, teacher_name) values (2,'muhammed');")
        curr.execute("INSERT INTO teachers (teacher_id, teacher_name) values (3,'rex');")

        print('---students----')
        curr.execute('SELECT * FROM students')
        results=curr.fetchall()
        for item in results:
            print(item)

        print('\n---teachers----')
        curr.execute('SELECT * FROM teachers')
        results=curr.fetchall()
        for item in results:
            print(item)


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)      
    finally: 
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    

if __name__ == '__main__':
    connect()


