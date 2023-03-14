import psycopg2


def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost", database="Pagila DB", user="postgres", password=123456
        )
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    conn.autocommit = True

    cur.execute("SELECT * from actor;")
    print(cur.fetchall())
    print("---------------------------")
    cur.execute("SELECT * FROM category;")
    print(cur.fetchone())
    print("---------------------------")
    cur.execute("SELECT * from address;")
    print(cur.fetchmany(50))
    cur.close()


if __name__ == "__main__":
    connect()
