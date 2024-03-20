#!/usr/bin/python3
"""
    The `All cities by state` module
"""
import MySQLdb
import sqlalchemy
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=user,
                           passwd=passwd,
                           db=db,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("""
                    SELECT cities.name FROM cities
                    INNER JOIN states
                    ON cities.state_id=states.id
                    WHERE states.name = "{}"
                    GROUP BY cities.name
                """.format(name))
    query_rows = cur.fetchall()
    for i in range(len(query_rows)):
        if i != len(query_rows) - 1:
            print(query_rows[i][0], end=', ')
        else:
            print(query_rows[i][0])
    cur.close()
    conn.close()
