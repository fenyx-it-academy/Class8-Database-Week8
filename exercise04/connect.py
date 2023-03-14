
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
        
        print("All rows from the actor table:")
        cur.execute('SELECT * FROM public."actor"')
        res = cur.fetchall()
        for row in res:
            print(row)
            
        print("First row from the category table:")
        cur.execute('SELECT * FROM public."category"')
        res = cur.fetchone()
        print(res)
        
        print("First 50 rows from the address table:")
        cur.execute('SELECT * FROM public."address"')
        res = cur.fetchmany(50)
        for row in res:
            print(row)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # close the communication with the PostgreSQL
            cur.close()
            conn.close()
            print('Database connection closed.')