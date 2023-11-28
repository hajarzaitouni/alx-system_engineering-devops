#!/usr/bin/python3
""" export data in the CSV format """
import json
import requests
import sys


if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    user = requests.get(url_user).json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            u.get("id"): [{
                "username": u.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed"),
            } for task in requests.get(url_todos,
                                       params={"userId": u.get("id")}).json()]
            for u in user}, f)
