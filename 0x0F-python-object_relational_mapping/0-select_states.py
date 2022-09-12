#!/usr/bin/python3
"""show all data in the database"""
import sys
import MySQLdb as mysql_

if __name__ == "__main__":
    conn = mysql_.connect("localhost", *sys.argv[1:])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id;")
    result = cur.fetchall()

    for state in result:
        print(state)
    cur.close()
    conn.close()
