import psycopg2
from config import config


def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        try:
            # try to connect to database
            params = config('database.ini','pagila_owner')
            conn = psycopg2.connect(**params)
		
            # create a cursor
            cur = conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            # if database doesn't exist, create it
            print(error)

        conn.autocommit = True # this command enables autocommit to postgreSQL otherwise at the end of each operation you must do conn.commit()
        curr = conn.cursor()
        cur.execute('SELECT * from actor;')
        print(cur.fetchall())
        cur.execute('SELECT * FROM category;')
        print(cur.fetchone())
        cur.execute('SELECT * from address;')
        print(cur.fetchmany(50))
        curr.close()  

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)      
    finally: 
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    

if __name__ == '__main__':
    connect()


