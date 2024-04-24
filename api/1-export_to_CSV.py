#!/usr/bin/python3
"""Export data in the CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        exit(1)
    userId = sys.argv[1]
    user = requests.get("{}/users/{}".format(API_URL, userId)).json()

    if not user:
        print("No employee record found for ID: {}".format(userId))
        exit(1)

    tasks = requests.get("{}/todos?userId={}".format(API_URL, userId)).json()

    with open("{}.csv".format(userId), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([userId, user.get("username"), task.get("completed"),
                          task.get("title")]) for task in tasks]
