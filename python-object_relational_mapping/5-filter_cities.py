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
    cur.execute("SELECT 
