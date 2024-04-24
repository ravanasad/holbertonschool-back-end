#!/usr/bin/python3
"""export data in the json format."""
import json
import requests


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(API_URL)).json()
    tasks = requests.get("{}/todos".format(API_URL)).json()
    dictionary = {}
    for user in users:
        user_id = user['id']
        user_tasks = [task for task in tasks if task['userId'] == user_id]

        dictionary[user_id] = [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
                } for task in user_tasks]

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(dictionary, jsonfile)
