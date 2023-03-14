import psycopg2

conn = None

conn = psycopg2.connect(
    host = "localhost",
    database = "DB_DATABASE",
    user = "postgres",
    password = "12345678"
)
conn.autocommit = True
cur = conn.cursor()
cur.execute("SELECT * FROM actor;")
result = cur.fetchall()
print(result)
for result in result : 
    print(result)

print("----------------------------------------------------------------------------------------------")
cur.execute("SELECT * FROM category;")
first_row = cur.fetchone()
print(first_row)
print("------------------------------------------------------------------------------------------------")
cur.execute("SELECT * FROM address;")
first_50_rows = cur.fetchmany(50) 
print("-------------------------",len(first_50_rows),"-------------------------------------------")
print(first_50_rows)
conn.close()