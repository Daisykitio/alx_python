import json
import requests
import sys

def fetch_employee_data(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Make a GET request to fetch employee details
    employee_response = requests.get(base_url + f"users/{employee_id}")
    employee_data = employee_response.json()

    if employee_response.status_code != 200:
        print(f"Error: Unable to fetch employee data for ID {employee_id}")
        return

    # Make a GET request to fetch TODO list for the employee
    todo_response = requests.get(base_url + f"users/{employee_id}/todos")
    todo_list = todo_response.json()

    if todo_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return

    # Create a JSON object for the employee's tasks
    employee_tasks = {str(employee_id): []}

    # Add each task to the JSON object
    for task in todo_list:
        employee_tasks[str(employee_id)].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_data['username']
        })

    # Create a JSON file for the employee's tasks
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(employee_tasks, json_file, indent=4)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_data(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer.")

