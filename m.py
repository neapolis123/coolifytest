import psycopg2
import time
import os

conn = psycopg2.connect(os.getenv('DATABASE_URL',None))

cur = conn.cursor()

result = cur.execute("INSERT INTO cars VALUES ('Aston Martin', 'Vanquish', 2019)" )
conn.commit()
print('successful insert')

while True:
    time.sleep(5)
    print('slept for 5s')
