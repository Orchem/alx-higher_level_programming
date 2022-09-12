#!/usr/bin/python3
"""list cities by state"""
from sys import argv
import MySQLdb as mysql_

if __name__ == "__main__":
    connection = mysql_.connect("localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    cur = connection.cursor()

    query = """SELECT cities.id, cities.name, states.name FROM cities
    JOIN states WHERE cities.state_id = states.id ORDER BY cities.id;"""

    cur.execute(query)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    connection.close()
