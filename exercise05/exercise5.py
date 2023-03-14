
import psycopg2
from configparser import ConfigParser
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
database_path = os.path.join(dir_path, 'database.ini')

def config(filename=database_path, section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    print(parser.items())
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return [conn, cur]
    

if __name__ == '__main__':
    
    try:
        [conn, cur] = connect()
        
        print("Creating students table if it doesn't exist...")
        cur.execute('''CREATE TABLE IF NOT EXISTS students (
                        student_id serial PRIMARY KEY,
                        name VARCHAR ( 50 ) NOT NULL
                        );''')
        print("Done!")
        
        print("Creating teachers table if it doesn't exist...")
        cur.execute('''CREATE TABLE IF NOT EXISTS teachers (
                        teacher_id serial PRIMARY KEY,
                        name VARCHAR ( 50 ) NOT NULL
                        );''')
        print("Done!")
        
        
        print("Inserting 3 rows to students table if they don't exist...")
        cur.execute('''INSERT INTO students(student_id, name) VALUES
                        (1, 'John'),
                        (2, 'Jane'),
                        (3, 'Jack')
                        ON CONFLICT (student_id) DO NOTHING;''')
        print("Done!")
        
        print("Inserting 3 rows to teachers table if they don't exist...")
        cur.execute('''INSERT INTO teachers(teacher_id, name) VALUES
                        (1, 'Marry'),
                        (2, 'Blake'),
                        (3, 'Ethan')
                        ON CONFLICT (teacher_id) DO NOTHING;''')
        print("Done!")
        
        print("Student table:")
        cur.execute('''SELECT * FROM students''')
        result = cur.fetchall()
        for row in result:
            print(row)
        print("---------------------")
        
        
        print("Teachers table:")
        cur.execute('''SELECT * FROM teachers''')
        result = cur.fetchall()
        for row in result:
            print(row)
        print("---------------------")
    
            
        
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # close the communication with the PostgreSQL
            cur.close()
            conn.close()
            print('Database connection closed.')