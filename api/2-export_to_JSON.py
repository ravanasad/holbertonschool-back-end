#!/usr/bin/python3
import requests
import sys
import csv
import urllib
import json


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
    dictionary = {
        userId: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in tasks]
    }
    with open("{}.json".format(userId), "w") as jsonfile:
        json.dump(dictionary, jsonfile)
