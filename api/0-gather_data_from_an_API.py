#!/usr/bin/python3
"""Gather data from an API"""
import requests
import urllib
import sys


API_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        exit(1)
    userId = sys.argv[1]
    user = requests.get("{}/users/{}".format(API_URL, userId)).json()

    if not user:
        print("No employee record found for ID: {}".format(userId))
        exit(1)

    tasks = requests.get("{}/todos?userId={}".format(API_URL, userId)).json()
    completed_tasks = [task for task in tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(tasks)))
    [print("\t {}".format(task.get("title"))) for task in completed_tasks]
