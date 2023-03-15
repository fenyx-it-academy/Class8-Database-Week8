import psycopg2
import os
from config import config

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
        table_name = 'address'
        os.system('cls')
        col_headers = ['address_id', 'address', 'address2', 'district', 'city_id', 'postal_code', 'phone', 'last_update']
        print('{:12}   {:40}  {:10}  {:25}  {:5}  {:11}  {:13} {}'.format(*col_headers))
        print('-'*150)
        # get query data
        cur.execute('SELECT address_id, address, address2, district, city_id, postal_code, phone, last_update FROM "{}"'.format(table_name))
        data = cur.fetchmany(50)
        for row in data:
            i = list(row)
            for f in range(len(row)):
                if i[f] == None:
                    i[f] = ''
            print('{:12d}   {:40}  {:10}  {:25}  {:5d}  {:11}  {:13} {}'.format(*list(i)))
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()
    