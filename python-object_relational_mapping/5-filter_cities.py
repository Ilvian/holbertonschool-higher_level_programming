#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


if __name__ == "__name__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cur = db.cursor()
    with db.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %(state_name)s \
            ORDER BY cities.id ASC", {'state_name': sys.argv[4]})

        rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))

    cur.close()
    db.close()
