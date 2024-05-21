#!/usr/bin/python3
""" Script to create dictionary of dict from an api
"""
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    data_dict = {}

    for user in users:
        user_id = user.get("id")
        data_dict[user_id] = []
        urll = "https://jsonplaceholder.typicode.com/todos/"
        todos = requests.get(urll+'?userId={}'.format(user_id)).json()
        for todo in todos:
            new_dict = {
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                    }
            data_dict[user_id].append(new_dict)

    with open("todo_all_employees.json", "w") as jfile:
        json.dump(data_dict, jfile)
