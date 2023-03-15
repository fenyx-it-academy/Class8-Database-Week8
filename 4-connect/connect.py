import psycopg2
def connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "pagila2",
            user = "postgres",
            password = "123321")
        cur = conn.cursor()
        cur.execute('SELECT * FROM public.actor ')
        actor_rows = cur.fetchall()
        print(actor_rows)
        cur.execute('SELECT * FROM public.category')
        catagory_first_row = cur.fetchone()
        print(catagory_first_row)
        cur.execute('SELECT * FROM public.address')
        address_50_rows = cur.fetchmany(50)
        print(address_50_rows)
        cur.execute('SELECT * FROM public.language')
        language_rows=cur.fetchall()
        print(language_rows)


        cur.close()
    except(Exception,psycopg2.DatabaseError) as Error:
        print(Error)
    finally:
        if conn is not None:
            cur.close()
if __name__ == '__main__':
    connection()