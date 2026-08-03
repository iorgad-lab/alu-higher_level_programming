#!/usr/bin/python3
"""Displays values where name matches argument (vulnerable to SQL injection)."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM `states` WHERE `name` = '{}' ORDER BY `id`"
    cur.execute(query.format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
