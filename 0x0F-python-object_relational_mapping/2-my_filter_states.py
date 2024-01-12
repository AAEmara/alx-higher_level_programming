#!/usr/bin/python3
"Module 2-my_filter_states that uses MySQLdb Library."
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name = '{}'
        ORDER BY id;""".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
