#!/usr/bin/python3
"""
Module for script that takes an argument and displays all value in the
states table where name matches the argument
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

    sql_cmd = "SELECT cities.id, cities.name, states.name FROM cities, states\
               WHERE cities.state_id=states.id ORDER BY cities.id"
    cur.execute(sql_cmd)
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
