#!/usr/bin/python3
"""
extends Python script to export data in the CSV format
"""
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

    filename = '{}.csv'.format(arg)
    with open(filename, 'w') as csvfile:
        for details in employee_todo:
            status = details.get('completed')
            user_id = details.get('userId')
            title = details.get('title')
            fields = '"{}","{}","{}","{}"\n'.format(
                user_id, username, status, title)
            csvfile.write(fields)
