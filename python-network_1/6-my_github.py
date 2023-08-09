#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: {} <username> <personal_access_token>".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

url = 'https://api.github.com/user'
response = requests.get(url, auth=(username, personal_access_token))

try:
    user_data = response.json()
    print(user_data.get('id'))
except ValueError:
    print("None")

