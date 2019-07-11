import psycopg2

conn = psycopg2.connect(dbname="huricane", user='ihw_admin', password="admin")
cur = conn.cursor()

with open("to_load.csv","r") as f:
	cur.copy_expert("COPY huricane_main FROM STDIN WITH CSV",f)

conn.commit()