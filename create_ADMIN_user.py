import psycopg2

conn = psycopg2.connect(dbname='huricane', user='postgres', password='postgres')
cur = conn.cursor()

#cur.execute("CREATE USER IHW_admin with PASSWORD 'admin' NOSUPERUSER")
cur.execute("GRANT SELECT, UPDATE, INSERT ON huricane_main TO IHW_admin")

conn.commit()