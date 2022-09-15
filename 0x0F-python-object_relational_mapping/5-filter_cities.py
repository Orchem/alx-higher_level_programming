#!/usr/bin/python3
"""List all states from a database starting with N"""
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(port=3306, user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT `c`.`name` \
    FROM `cities` as `c` \
    INNER JOIN `states` as `s` \
    ON `c`.`state_id` = `s`.`id` \
    WHERE `s`.`name`=%s \
    ORDER BY `c`.`id`;", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
