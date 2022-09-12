#!/usr/bin/python3
"""prevention again SQL injection with prepared statements"""
import sys
import MySQLdb as mysql_


if __name__ == "__main__":
    conn = mysql_.connect("localhost", *sys.argv[1:-1])
    cur = conn.cursor()
    query = """SELECT * FROM states
        WHERE states.name = %s
        ORDER BY states.id;
    """

    cur.execute(query, (sys.argv[-1], ))
    result = cur.fetchall()

    for state in result:
        print(state)

    cur.close()
    conn.close()
