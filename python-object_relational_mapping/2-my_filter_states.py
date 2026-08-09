#!/usr/bin/python3
"""Script that lists states matching a user-provided name."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"
    cur.execute(query.format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
