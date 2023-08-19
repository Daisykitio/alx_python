#!/usr/bin/env python3
"""
Script to list all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

def list_cities_by_state(username, password, database):
    """Fetches and displays all cities from the database hbtn_0e_4_usa"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities_by_state(username, password, database)

