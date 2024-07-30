#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON."""
import requests
import sys
import json


def fetch_and_export_todo_json(employee_id):
    """
    Retrieve and export to-do list for an employee to a JSON file.
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

    username = user_data.get("username")
    formatted_tasks = [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
                }
            for task in todo_list
            ]

    json_data = {str(employee_id): formatted_tasks}

    file_name = f"{employee_id}.json"
    with open(file_name, 'w') as json_file:
        json.dump({str(employee_id): tasks}, file, indent=4)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    fetch_and_export_todo_json(employee_id)
