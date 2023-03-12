import psycopg2
from config import *




try:

    # read connection parameters
    params = pagila_db()

    # connect to the PostgreSQL server
    #print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)
    # create a cursor
    cur = conn.cursor()


    print (f"##############################################")
    print (f"##############################################")
    print (f"Printing all rows in the table actor.")
    print (f"##############################################")
    print (f"##############################################")

    cur.execute("SELECT * FROM public.actor")
    rows = cur.fetchall()
    for row in rows:
        print (row)
    
    print (f"##############################################")
    print (f"##############################################")
    print (f"Finished printing all rows in the table actor.")
    print (f"##############################################")
    print (f"##############################################")





    print (f"##############################################")
    print (f"##############################################")
    print (f"Printing first row of `category` table")
    print (f"##############################################")
    print (f"##############################################")

    cur.execute("SELECT * FROM public.category LIMIT 1")
    row = cur.fetchone()
    print (row)

    print (f"##############################################")
    print (f"##############################################")
    print (f"Finished printing first row of `category` table")
    print (f"##############################################")
    print (f"##############################################")






    print (f"##############################################")
    print (f"##############################################")
    print (f"Printing first 50 rows of `address` table")
    print (f"##############################################")
    print (f"##############################################")

    cur.execute("SELECT * FROM public.address LIMIT 50")
    rows = cur.fetchall()
    for row in rows:
        print (row)

    print (f"##############################################")
    print (f"##############################################")
    print (f"Finished printing first 50 rows of `address` table")
    print (f"##############################################")
    print (f"##############################################")

except (Exception, psycopg2.Error) as error:
    print("error: ", error)

finally:
    # closing database connection.
    if conn:
        cur.close()
        conn.close()
        #print("PostgreSQL connection is closed")
