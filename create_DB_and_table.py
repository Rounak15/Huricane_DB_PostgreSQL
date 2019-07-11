import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres')
conn.autocommit = True
cur = conn.cursor()
cur.execute("DROP DATABASE IF EXISTS huricane")
cur.execute("CREATE DATABASE huricane")
conn.close()

conn_hur = psycopg2.connect(dbname='huricane', user='postgres', password='postgres')
cur = conn_hur.cursor()

cur.execute("DROP TABLE IF EXISTS huricane_main")
cur.execute("""CREATE TABLE huricane_main (
			fid INTEGER PRIMARY KEY,
			huricane_date TIMESTAMP with time zone,
			btid SMALLINT,
			name TEXT  ,
			latitude DECIMAL(4, 1)  ,
			longitude DECIMAL(4, 1) ,
			wind_kts INTEGER  ,
			pressure INTEGER  ,
			cat  CHAR(2),
			basin TEXT ,
			shape_length DECIMAL(10, 6)
			)
			""")

conn_hur.commit()