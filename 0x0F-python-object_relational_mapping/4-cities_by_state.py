#!/usr/bin/python3
"""A module for connecting and executing a select statement in MySQLdb."""

if __name__ == "__main__":
    import sys
    import MySQLdb

    args = sys.argv
    db = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()

    query = "SELECT c.id, c.name, s.name\
             FROM cities AS c\
             JOIN states AS s\
             ON c.state_id = s.id\
             ORDER BY c.id ASC;"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
