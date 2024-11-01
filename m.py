import psycopg2


conn = psycopg2.connect("postgres://postgres:3QUHdz5M0KbCVK68m5lZmMPN0ontmaXIHZL0rTuvjXe2gvryLldXE6z3i1UHySac@rg8wc8so4sc8o44wowwos08g:5432/cars" )

cur = conn.cursor()

result = cur.execute("INSERT INTO cars VALUES ('Audi', 'A5', 2024)" )
conn.commit()
print(result)
