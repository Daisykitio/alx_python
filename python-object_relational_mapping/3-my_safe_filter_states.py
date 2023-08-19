#!/usr/bin/env python3
"""
Script to safely list states where the name matches the provided argument from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

def safe_filter_states_by_name(username, password, database, search_name):
    """Safely fetches and displays states where the name matches the provided argument"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (search_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <search_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_name = sys.argv[4]

    safe_filter_states_by_name(username, password, database, search_name)

