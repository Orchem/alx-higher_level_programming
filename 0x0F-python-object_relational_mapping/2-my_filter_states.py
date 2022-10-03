#!/usr/bin/python3
"""list db entry for a specific state"""
from sys import argv
import MySQLdb as mysql_

if __name__ == "__main__":
    conn = mysql_.connect(
        host="localhost", port=3306, user=argv[1],
        passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
