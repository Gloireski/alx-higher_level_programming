#!/usr/bin/python3
# Belem Gloire BEKOUTOU
# 0-select_states.py
"""script that takes in an argument and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument.
    Args:
        mysql username;
        mysql password;
        database name;
        state name searched
    module: MySQLdb (import MySQLdb)
    server: localhost at port 3306
    Results must be sorted in ascending order by states.id
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = '{}'"
              .format(sys.argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
