#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"
    userId = int(sys.argv[1])
    user = requests.get("{}/users/{}".format(API_URL, userId)).json()

    tasks = requests.get("{}/todos?userId={}".format(API_URL, userId)).json()
    completed_tasks = [task for task in tasks if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(tasks)))
    [print("\t {}".format(task.get("title"))) for task in completed_tasks]
