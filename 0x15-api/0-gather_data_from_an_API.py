#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given
employee ID, returns information about his/her Todo list progress
a Python script that, using this REST API, for a given
employee ID, returns information about his/her Todo list progress
a Python script that, using this REST API, for a given
employee ID, returns information about his/her Todo list progress
a Python script that, using this REST API, for a given
employee ID, returns information about his/her Todo list progress
employee ID, returns information about his/her Todo list progress
employee ID, returns information about his/her Todo list progress
employee ID, returns information about his/her Todo list progress
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    # parameter for employee id
    param = argv[1]
    employee_by_id = requests.get(url + f'users/{param}').json()
    name = employee_by_id.get('name')
    payload = {"userId":  param}
    employee_todo = requests.get(url + f'todos/', params=payload).json()

    done_task = 0
    get_tasks_done = []
    for task in employee_todo:
        if task.get("completed"):
            get_tasks_done.append(task)
            done_task += 1
    num_tasks = len(employee_todo)
    print(f"Employee {name} is done with tasks({done_task}/{num_tasks})")

    for task in get_tasks_done:
        title = task.get('title')
        print(f"\t {title}")
