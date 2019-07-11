import psycopg2
from pprint import PrettyPrinter

pp = PrettyPrinter(indent = 2)

conn_hur = psycopg2.connect(dbname='huricane', user='postgres', password='postgres')
cur = conn_hur.cursor()
cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'huricane_main'")
columns = cur.fetchall()
pp.pprint(columns)
conn_hur.close()



