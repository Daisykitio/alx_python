#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: {} <URL> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

payload = {'email': email}
response = requests.post(url, data=payload)

print(response.text)

