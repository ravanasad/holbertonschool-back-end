#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        res = requests.get('https://jsonplaceholder.typicode.com/users/' +
                           f'{sys.argv[1]}/todos')
    response = json.loads(res.text)
    all_task = len(response)
    done_task = 0
    done_task_title = ""
    for task in response:
        if task["completed"] is True:
            done_task_title += "\t " + task["title"] + "\n"
            done_task = done_task + 1
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        f'{sys.argv[1]}')
    user_response = json.loads(user.text)
    user_name = user_response["name"]
    print(f"Employee {user_name} is done with tasks({done_task}/{all_task}):")
    print(done_task_title, end="")
