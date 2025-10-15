import os
import json
from datetime import datetime, date

DATABASE_URL = "database.json"

DELETEDTASKS_URL = "deletedtasks.json"

if not os.path.exists(DATABASE_URL):
    with open(DATABASE_URL, "w") as f:
        f.write("[]")


if not os.path.exists(DATABASE_URL):
    with open(DATABASE_URL, "w") as f:
        f.write("[]")


def read_database() -> list[dict]:
    with open(DATABASE_URL) as f:
        tasks = json.load(f)

    return tasks


def read_deletedtasks() -> list[dict]:
    with open(DELETEDTASKS_URL) as f:
        tasks = json.load(f)

    return tasks


def save_database(tasks: list[dict]):
    with open(DATABASE_URL, "w") as f:
        json.dump(tasks, f, indent=4)


def save_Deletedtasks(tasks: list[dict]):
    with open(DELETEDTASKS_URL, "w") as f:
        json.dump(tasks, f, indent=4)


def date_strftime_tasks(tasks):
    pastasks = list(map(lambda t: {
        **t,
        "due_date": t["due_date"].strftime("%d/%m/%Y"),
        "created_date": t["created_date"].strftime("%d/%m/%Y, %H:%M:%S")
    }, tasks))
    
    return pastasks



def create_task(name: str, description: str, category: str, date: date) -> bool:
    tasks = read_database()

    last_task = max(tasks, key=lambda task: task['id'], default={"id": 0})
    tasks.append({
        "id": last_task["id"] + 1,
        "name": name,
        "description": description,
        "category": category,
        "due_date": date.strftime("%d/%m/%Y"),
        "created_date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "status": False,
    })

    save_database(tasks)


def get_tasks():
    tasks = list(map(
        lambda task: {
            "id": task["id"],
            "name": task["name"],
            "description": task["description"],
            "category": task["category"],
            "due_date": datetime.strptime(task["due_date"], "%d/%m/%Y"),
            "created_date": datetime.strptime(task["created_date"], "%d/%m/%Y, %H:%M:%S"),
            "status": task["status"]
        },
        read_database(),
    ))

    return tasks


def get_Deleted_tasks():
    tasks = list(map(
        lambda task: {
            "id": task["id"],
            "name": task["name"],
            "description": task["description"],
            "category": task["category"],
            "due_date": datetime.strptime(task["due_date"], "%d/%m/%Y"),
            "created_date": datetime.strptime(task["created_date"], "%d/%m/%Y, %H:%M:%S"),
            "status": task["status"]
        },
        read_deletedtasks(),
    ))

    return tasks

