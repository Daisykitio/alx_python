import requests
import sys

def fetch_employee_data(employee_id):
    """
    Fetch and display employee data and their TODO list progress from an API.
    
    Args:
        employee_id (int): The ID of the employee to fetch data for.
    """
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Make a GET request to fetch employee details
    employee_response = requests.get(f"{base_url}users/{employee_id}")
    employee_data = employee_response.json()

    if employee_response.status_code != 200:
        print(f"Error: Unable to fetch employee data for ID {employee_id}")
        return

    # Make a GET request to fetch TODO list for the employee
    todo_response = requests.get(f"{base_url}users/{employee_id}/todos")
    todo_list = todo_response.json()

    if todo_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return

    # Calculate the number of completed and total tasks
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task["completed"])

    # Display the employee's TODO list progress
    print(f"Employee {employee_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")
    
    for task in todo_list:
        if task["completed"]:
            print(f"    {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_data(employee_id)
        except ValueError as e:
            print(f"Error: {e}. Employee ID must be an integer.")

