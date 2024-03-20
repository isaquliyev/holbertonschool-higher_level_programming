#!/usr/bin/python3

import MySQLdb
import sqlalchemy
import sys

argv = sys.argv
user = argv[1]
passwd = argv[2]
db = argv[3]

conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db, charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
