#!/usr/bin/python3
""" export data in the CSV format """
import requests
import sys
import csv


if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    user = requests.get(url_user + "{}".format(sys.argv[1])).json()
    todos = requests.get(url_todos, params={"userId": sys.argv[1]}).json()

    user_id = sys.argv[1]
    user_name = user.get("name")

    with open("{}.csv".format(user_id), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, user_name,
                             task.get("completed"), task.get("title")])
