#!/usr/bin/python3
"Module 0-select_states that uses MySQLdb Library."
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC;""")
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
