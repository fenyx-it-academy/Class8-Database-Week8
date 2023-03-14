import psycopg2
from config import config


def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        try:
            # try to connect to database
            params = config('database.ini','PyCoders')
            conn = psycopg2.connect(**params)
		
            # create a cursor
            cur = conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            # if database doesn't exist, create it
            print(error)

        conn.autocommit = True # this command enables autocommit to postgreSQL otherwise at the end of each operation you must do conn.commit()
        curr = conn.cursor()
            
        curr.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        table_names = curr.fetchall()
        
        if len(table_names) != 0:
            print("Database tables are already created!")
            print("Existing tables:")
            for table in table_names:
                cur.execute(f'SELECT * FROM {table[0]};')  
                print(table)
                print(cur.fetchall())
        else:
            file = open('PyCoders_sql.sql', 'r')
            sqlFile = file.read()
            file.close()
            # all SQL commands (split on ';')
            sqlCommands = sqlFile.split(';')[:-1]
            # Execute every command from the input file
            for command in sqlCommands:
                try:
                    curr.execute(command)
                except (Exception, psycopg2.DatabaseError) as error:
                    print("Command skipped: ", error)
                    break
            curr.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            print(len(curr.fetchall()), ' tables created.')
            cur.execute('SELECT * FROM students;')
            print(cur.fetchall())
            cur.execute('SELECT * from teachers;')
            print(cur.fetchall())
            curr.close()  

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)      
    finally: 
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    

if __name__ == '__main__':
    connect()


