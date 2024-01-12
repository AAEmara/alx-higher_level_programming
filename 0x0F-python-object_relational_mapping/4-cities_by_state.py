#!/usr/bin/python3
"Module 4-cities_by_state that uses MySQLdb Library."
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM states AS s
        LEFT JOIN cities AS c
        ON c.state_id = s.id
        ORDER BY c.id ASC;""")
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}', '{row[2]}')")
