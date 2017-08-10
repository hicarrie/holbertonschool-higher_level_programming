#!/usr/bin/python3
"""
Module for script that lists all states from database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE states.name\
                LIKE 'N%' ORDER BY states.id;")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
