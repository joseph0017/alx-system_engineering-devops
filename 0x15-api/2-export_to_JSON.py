#!/usr/bin/python3
"""
extends Python script to export data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    arg = argv[1]
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(arg)
    todos_url = 'https://jsonplaceholder.typicode.com/todos/'
    users = requests.get(users_url).json()
    username = users.get('username')
    payload = {"userId":  arg}
    employee_todo = requests.get(todos_url, params=payload).json()

    array = {arg: []}
    for details in employee_todo:
        status = details.get('completed')
        title = details.get('title')
        array[arg].append({
                                    "task": title,
                                    "completed": status,
                                    "username": username
                                    })
    filename = '{}.json'.format(arg)
    with open(filename, 'w') as jsonfile:
        json.dump(array, jsonfile)
