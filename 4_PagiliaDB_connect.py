import psycopg2

def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        try:
            # try to connect to database
            conn = psycopg2.connect(
                host="localhost",
                database="PagiliaDB",
                user="postgres",
                password="1")
        except (Exception, psycopg2.DatabaseError) as error:
            pass
       

        conn.autocommit = True # this command enables autocommit to postgreSQL otherwise at the end of each operation you must do conn.commit()
        # In[Fun part]
        curr = conn.cursor()   
        
        print('--------all rows from actor table---------')
        curr.execute('SELECT * FROM public."actor" ')
        results=curr.fetchall()
        for result in results:
            print (result)
        print('------first row of category table-----------')
        curr.execute('SELECT * FROM public."category" ')
        results=curr.fetchone()
        print(results)
      
        print('-------first 50 rows of adress table----------')
        curr.execute('SELECT * FROM public."address"  ')
        results=curr.fetchmany(50)
        for result in results:
            print (result)
        print('-----------------')
        
  
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)      
    finally: 
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    

if __name__ == '__main__':
    connect()


