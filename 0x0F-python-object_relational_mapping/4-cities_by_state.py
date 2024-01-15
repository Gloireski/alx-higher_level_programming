#!/usr/bin/python3
# Belem Gloire BEKOUTOU
# 4-cities_by_state.py
"""script that lists all cities from the database hbtn_0e_4_usa:
    Args:
        mysql username;
        mysql password;
        database name;
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
    c.execute("""SELECT cities.id, cities.name, states.name
               FROM cities, states WHERE states.id=cities.state_id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
