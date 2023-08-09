#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if isinstance(json_response, dict):
            if json_response:
                print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
            else:
                print("No result")
        else:
            print("Not a valid JSON")
    except ValueError:
        print("Not a valid JSON")

