import psycopg2
import os
from config import config
import termtables

# creates teachers and students table
def create_tables():
    tables = {
        'students': ['student_id SERIAL PRIMARY KEY', 'name VARCHAR(255) NOT NULL'],
        'teachers': ['teacher_id SERIAL PRIMARY KEY', 'name VARCHAR(255) NOT NULL']
    }
    conn = None
    try:
        params = config()
        params["database"] = "PyCoders"         # replace database attribute in database.ini with "PyCoders" 
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for tname, colnames in tables.items():
            cur.execute('CREATE TABLE IF NOT EXISTS {} ({})'.format(tname, ', '.join(colnames)))
            conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
# inserts data rows to specified table            
def insert_list(lst, table):
    sql = "INSERT INTO {} (name) VALUES(%s)".format(table)
    conn = None
    try:
        params = config()
        params["database"] = "PyCoders"
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, lst)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        
# prints tabular formatted table data in terminal screen  
def show_all(table):
    sql = 'SELECT * FROM "{}"'.format(table)
    col_headers = {
        'students': ['student_id', 'name'],
        'teachers': ['teacher_id' ,'name']
    }
    conn = None
    try:
        params = config()
        params["database"] = "PyCoders"
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        termtables.print(
            data,
            col_headers[table],
            style=termtables.styles.markdown
        )   
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('\nDatabase connection closed.\n')

if __name__ == '__main__':
    create_tables()
    teacher_list = [('Zeliha Dogan',), ('Jale Cerezci',), ('Sehri Memis',)]
    student_list = [('Murat Han',), ('Ebru Gul',), ('Fevzi Yildiz',)]
    # insert_list(teacher_list, "teachers")
    # insert_list(student_list, "students")
    show_all("teachers")
    show_all("students")
