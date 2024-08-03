# System Engineering Devops - API

## Description

This project involves gathering data from a REST API and exporting it in different formats such as CSV and JSON. The goal is to create Python scripts that interact with an API to fetch employee data and export it into various data structures. The key aspects of this project include understanding the use of REST APIs, handling JSON and CSV formats, gathering data from a REST API and exporting data.

## Project Structure

| Task                                | Description                                                                      | Source Code                                   |
|-------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------|
| Gather data from an API             | Using the provided REST API, return information about an employee's TODO list.   | [Link to code](path/to/code)                  |
| Export to CSV                       | Extend your Python script to export data in the CSV format.                      | [Link to code](path/to/code)                  |
| Export to JSON                      | Extend your Python script to export data in the JSON format.                     | [Link to code](path/to/code)                  |
| Dictionary of list of dictionaries  | Extend your Python script to export data in a dictionary of list of dictionaries.| [Link to code](path/to/code)                  |


## Features

1. **Accessing API Data**:
   - Use the `requests` library to fetch data from the provided API endpoints.
   - Handle different HTTP methods as required (GET, POST, etc.).

2. **Organizing Data**:
   - Parse JSON responses and organize the data into Python data structures (e.g., dictionaries, lists).

3. **Exporting Data**:
   - Export the organized data to CSV format.
   - Ensure data is correctly formatted and includes appropriate headers.

## Learning Objectives
- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic Package and module name style
- Pythonic Class name style
- Pythonic Variable name style
- Pythonic Function name style
- Pythonic Constant name style
- Significance of CapWords or CamelCase in Python
- Understand how to interact with a REST API using Python.
- Learn to handle data and export it in different formats.

## Environment

- Ubuntu 20.04 LTS
- Python 3.8.5
- `urllib` or `requests` module
- pycodestyle (version 2.8.*)

## Requirements
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Libraries imported in your Python files must be organized in alphabetical order
- All your files must be executable
- You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using if __name__ == "__main__":)

## How to Use

1. **Gather data from an API**
    - Script accepts an integer as a parameter, which is the employee ID.
    - Outputs the employee's TODO list progress.

2. **Export to CSV**
    - Exports all tasks owned by the employee in CSV format.
    - File named as `USER_ID.csv`.

3. **Export to JSON**
    - Exports all tasks owned by the employee in JSON format.
    - File named as `USER_ID.json`.

4. **Dictionary of list of dictionaries**
    - Exports all tasks from all employees in JSON format.
    - File named as `todo_all_employees.json`.

## Additional Info

- Ensure you have the necessary permissions to access the API.
- Test your scripts with different employee IDs to verify functionality.


## Tasks

1. **Gather data from an API**
    - Using the provided `REST API`, for a given employee ID, returns information about his/her TODO list progress.
    - Requirements:
        - You must use `urllib` or `requests` module
        - The script must accept an integer as a parameter, which is the employee ID
        - Display on the standard output: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
            - EMPLOYEE_NAME: name of the employee
            - NUMBER_OF_DONE_TASKS: number of completed tasks
            - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
        - Display the title of completed tasks: `TASK_TITLE`

Example:
```bash
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4
Employee Patricia Lebsack is done with tasks(6/20):
     odit optio omnis qui sunt
     doloremque aut dolores quidem fuga qui nulla
     sint amet quia totam corporis qui exercitationem commodi
     sequi dolorem sed
     eum ipsa maxime ut
     tempore molestias dolores rerum sequi voluptates ipsum consequatur
sylvain@ubuntu$
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T" 
EmployeeSPatriciaSLebsackSisSdoneSwithStasks(6/20):
TSoditSoptioSomnisSquiSsunt
TSdoloremqueSautSdoloresSquidemSfugaSquiSnulla
TSsintSametSquiaStotamScorporisSquiSexercitationemScommodi
TSsequiSdoloremSsed
TSeumSipsaSmaximeSut
TStemporeSmolestiasSdoloresSrerumSsequiSvoluptatesSipsumSconsequatur
sylvain@ubuntu$
```

2. **Export to CSV**
    - Using what you did in the task #0, extend your Python script to export data in the CSV format.
    - Requirements:
        - Records all tasks that are owned by this employee
        - Format must be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
        - File name must be: `USER_ID.csv`
Example:
```bash
sylvain@ubuntu$ python3 1-export_to_CSV.py 2
sylvain@ubuntu$ cat 2.csv
```

3. **Export to JSON**
    - Using what you did in the task #0, extend your Python script to export data in the JSON format.
    - Requirements:
        - Records all tasks that are owned by this employee
        - Format must be: `{ "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}`
        - File name must be: `USER_ID.json`
Example:
```bash
sylvain@ubuntu$ python3 2-export_to_JSON.py 2
sylvain@ubuntu$ cat 2.json
```

4. **Dictionary of list of dictionaries**
    - Using what you did in the task #0, extend your Python script to export data in the JSON format.
    - Requirements:
        - Records all tasks from all employees
        - Format must be: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
        - File name must be: `todo_all_employees.json`

Example:
```bash
sylvain@ubuntu$ python3 3-dictionary_of_list_of_dictionaries.py
sylvain@ubuntu$ cat todo_all_employees.json
```
