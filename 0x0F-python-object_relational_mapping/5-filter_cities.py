#!/usr/bin/python3
"""list cities from specific state"""
from sys import argv
import MySQLdb as mysql_

if __name__ == "__main__":
    connection = mysql_.connect("localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    cur = connection.cursor()

    query = """SELECT DISTINCT cities.name FROM cities
    JOIN states WHERE cities.state_id = (SELECT states.id FROM states
    WHERE states.name = %s ORDER BY cities.id);"""

    cur.execute(query, (argv[4],))

    print(", ".join(map(lambda x: x[0], cur.fetchall())))

    cur.close()
    connection.close()
