import psycopg2

def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        # try to connect to database
        conn = psycopg2.connect(
            host="localhost",
            database="Pagila",
            user="postgres",
            password="data")
        
        conn.autocommit = True # this command enables autocommit to postgreSQL otherwise at the end of each operation you must do conn.commit()
        curr = conn.cursor()
        curr.execute("SELECT * FROM actor")
        actors = curr.fetchall()
        print("All actors this BD:")
        for actor in actors:
            print(actor)

        curr.execute("SELECT * FROM category")
        category = curr.fetchone()
        print ("First category this DB:")
        print(category)

        curr.execute("SELECT * FROM address")
        address = curr.fetchmany(50)
        print ("First 50 address this DB:")
        print(address)

        curr.close()  

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)      
    finally: 
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    

if __name__ == '__main__':
    connect()