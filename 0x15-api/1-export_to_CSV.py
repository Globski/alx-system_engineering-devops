#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV."""
import csv
import requests
import sys

def fetch_and_export_todo_csv(employee_id):
    """
    Retrieve and export to-do list for an employee to a CSV file.
    Args:
        employee_id (int): The employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    todo_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todo_list = todo_response.json()

    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([employee_id, user_data.get("username"), task.get("completed"), task.get("title")])

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    fetch_and_export_todo_csv(employee_id)
