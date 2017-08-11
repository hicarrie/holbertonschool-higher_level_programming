#!/usr/bin/python3
"""
Module for script that takes the name of a state as an argument and lists all
cities of that state
"""


import sys
import MySQLdb

if __name__ == "__main__":
    state = sys.argv[4]
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)
    cur = db.cursor()

    sql_cmd = "SELECT cities.name FROM cities WHERE cities.state_id=(SELECT id\
              FROM states WHERE name='{}') ORDER BY cities.id".format(state,)
    cur.execute(sql_cmd)
    cities = cur.fetchall()
    separator = ""
    for city in cities:
        print(separator, end="")
        print(city[0], end="")
        separator = ", "
    print()
    cur.close()
    db.close()
