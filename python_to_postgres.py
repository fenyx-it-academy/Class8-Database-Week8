import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'schoolodev'
username = 'postgres'
pwd = 'Abdulrhman@774400167'
port_id = 5432
conn = None

try:
    with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS employee')

            create_script = ''' CREATE TABLE IF NOT EXISTS teachers (
                                    teacher_id      int PRIMARY KEY,
                                    teacher_name    varchar(40)) '''

            cur.execute(create_script)
            # insert_script = 'INSERT INTO teachers (teacher_id, teacher_name) VALUES (%s, %s)'
            # insert_values = [(1, 'Ronald'), (2, 'christain'), (3, 'Helen')]
            # for record in insert_values:
            #     cur.execute(insert_script, record)

            conn.commit()

            query_teacher = 'SELECT * FROM teachers WHERE teacher_name = %s'
            name = ["Ronald",]
            cur.execute(query_teacher, name)
            for record in cur.fetchall():
                print(record['teacher_id'], record['teacher_name'])

            cur.execute('SELECT * FROM students')
            for record in cur.fetchall():
                print(record['student_id'], record['name'])

            # update_script = 'UPDATE students SET salary = salary + (salary * 0.5)'
            # cur.execute(update_script)

            # delete_script = 'DELETE FROM employee WHERE name = %s'
            # delete_record = ('James',)
            # cur.execute(delete_script, delete_record)

            # cur.execute('SELECT * FROM EMPLOYEE')
            # for record in cur.fetchall():
            #     print(record['name'], record['salary'])
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
