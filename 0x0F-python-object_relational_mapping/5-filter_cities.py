#!/usr/bin/python3
"""A module for connecting and executing a select statement in MySQLdb."""

if __name__ == "__main__":
    import sys
    import MySQLdb

    args = sys.argv
    db = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()

    query = "SELECT c.name\
             FROM cities AS c\
             JOIN states AS s\
             ON c.state_id = s.id\
             WHERE s.name LIKE BINARY %s\
             ORDER BY c.id ASC;"
    cur.execute(query, (args[4],))
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        if (i < (len(rows) - 1)):
            print(row[0], end=', ')
        else:
            print(row[0], end='')
    print()
