#!/usr/bin/python3
import json
import requests


def fetch_data():
    """Fetch to-do list information of all employees from the API"""
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos_data = todos_response.json()

    users_response = requests.get(users_url)
    users_response.raise_for_status()
    users_data = users_response.json()

    return todos_data, users_data


def export_to_json(todos, users):
    """Export data to a JSON file"""
    users_dict = {user['id']: user['username'] for user in users}

    result = {}
    for task in todos:
        user_id = str(task['userId'])
        if user_id not in result:
            result[user_id] = []
        task_info = {
                "username": users_dict.get(int(user_id), "Unknown"),
                "task": task['title'],
                "completed": task['completed']
                }
        result[user_id].append(task_info)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(result, f, indent=4)


def main():
    todos_data, users_data = fetch_data()
    export_to_json(todos_data, users_data)


if __name__ == '__main__':
    main()
