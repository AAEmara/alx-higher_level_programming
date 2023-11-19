#!/usr/bin/python3
"""A module for connecting and executing a select statement in MySQLdb."""

if __name__ == "__main__":
    import sys
    import MySQLdb

    args = sys.argv
    db = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()

    query = "SELECT * FROM states\
                 WHERE states.name LIKE BINARY '{}'\
                 ORDER BY states.id ASC;".format(args[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
