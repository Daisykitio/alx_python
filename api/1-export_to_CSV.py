import csv
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

    # Create a CSV file for the employee's tasks
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task to the CSV file
        for task in todo_list:
            csv_writer.writerow([employee_id, employee_data['username'], str(task['completed']), task['title']])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_data(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer.")

