#!/usr/bin/python3
# Belem Gloire BEKOUTOU
# 5-filter_cities.py
"""script that takes in the name of a state as an argument and lists all cities
   of that state, using the database hbtn_0e_4_usa
    Args:
        mysql username;
        mysql password;
        database name;
        state name;
    module: MySQLdb (import MySQLdb)
    server: localhost at port 3306
    Results must be sorted in ascending order by states.id
    use only execute() once
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.name FROM cities
                 WHERE cities.state_id =
                 (SELECT states.id FROM states WHERE states.name = '{}')"""
              .format(sys.argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
