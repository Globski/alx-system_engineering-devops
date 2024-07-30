#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


def fetch_and_export_todo_json():
    """
    Retrieve and export to-do lists for all employees to a JSON file.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(base_url + "users").json()

    all_todos = {}

    for user in user_response:
        user_id = str(user.get("id"))

        todo_response = requests.get(
                base_url + "todos", params={"userId": user.get("id")}
                ).json()

        all_todos[user_id] = [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
            } for task in todo_response]

        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(all_todos, jsonfile, indent=4)


if __name__ == "__main__":
    fetch_and_export_todo_json()
