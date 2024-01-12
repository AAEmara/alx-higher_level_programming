#!/usr/bin/python3
"Module 5-filter_cities that uses MySQLdb Library."
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.name FROM states AS s
        JOIN cities AS c
        ON c.state_id = s.id
        WHERE s.name = BINARY %s
        ORDER BY c.id ASC;""", (sys.argv[4],))
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i < len(rows) - 1:
            print(rows[i][0], end=", ")
        elif i == len(rows) - 1:
            print(rows[i][0], end="")

    print()
