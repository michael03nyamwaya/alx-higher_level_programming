#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
<<<<<<< HEAD
                            <database name>
=======
                             <database name>
>>>>>>> 5d0a56274097ff078737b3755a1e6007b023a6c4
"""
import sys
import MySQLdb

if __name__ == "__main__":
<<<<<<< HEAD
db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM `states`")
[print(state) for state in c.fetchall()]


=======
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
>>>>>>> 5d0a56274097ff078737b3755a1e6007b023a6c4
