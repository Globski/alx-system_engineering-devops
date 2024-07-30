#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays employee's TODO list progress.
    Args:
        employee_id (int): The employee ID.
    """

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    todo_response = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    )
    todo_list = todo_response.json()

    employee_name = user_data.get("name")
    completed_tasks = [
        task.get("title") for task in todo_list if task.get("completed")
    ]

    print(f"Employee {employee_name} is done with tasks "
          f"({len(completed_tasks)}/{len(todo_list)}):")

    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
