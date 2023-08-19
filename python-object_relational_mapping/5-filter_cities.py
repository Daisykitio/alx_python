#!/usr/bin/env python3
"""
Script to list cities of a specified state from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

def filter_cities_by_state(username, password, database, state_name):
    """Fetches and displays cities of the specified state sorted by their IDs"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute

