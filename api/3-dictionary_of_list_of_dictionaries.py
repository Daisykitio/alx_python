#!/usr/bin/python3
"""
Export data in JSON format
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)
    users = response_users.json()
    todos = response_todos.json()
    
    all_data = {}
    
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        
        user_tasks = []
        
        for task in todos:
            if task.get('userId') == user_id:
                user_tasks.append({
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                })
        
        all_data[str(user_id)] = user_tasks
    
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_data, json_file)

