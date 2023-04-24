#!/usr/bin/python3
"""
extends Python script to export data in the JSON format
"""
import requests
import json


if __name__ == '__main__':
    users_url = f'https://jsonplaceholder.typicode.com/users/'
    todos_url = f'https://jsonplaceholder.typicode.com/todos/'
    users = requests.get(users_url).json()  
    employee_todo = requests.get(todos_url).json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        dictionary[user_id] = []
        for details in employee_todo:
            status = details.get('completed')
            title = details.get('title')
            employee_id = details.get('userId')
            dictionary[user_id].append({
                                        "task": title,
                                        "completed": status,
                                        "username": username
                                        })
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(dictionary, jsonfile)
