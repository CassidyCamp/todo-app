from datetime import datetime
import json

from rich.console import Console
from rich.table import Table

from .storage import (
    create_task,
    get_tasks,
    save_database,
    save_Deletedtasks,
    get_Deleted_tasks,
    date_strftime_tasks,
)


def add_task():
    name = input("Task name: ").strip().capitalize()
    description = input("Description: ").strip().capitalize()
    category = input("Category: ").strip().title()
    due_date = input("Date (example: 2025-10-11): ")

    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    
    if due_date < datetime.now():
        print("Date shoulde be greater than or equal to now.")
        return

    create_task(name, description, category, due_date)
    print("✅ Vazifa muvaffaqiyatli qo'shildi!")


def show_tasks(checkDetail=True, DeletedTasks=False):
    tasks = get_tasks()
    
    if DeletedTasks:
        tasks = get_Deleted_tasks()

    console = Console()

    table = Table(title="All Tasks")
    table.add_column("Number")
    table.add_column("Name")
    table.add_column("Category")
    table.add_column("Due Date")

    for num, task in enumerate(tasks, start=1):
        du_date = task["due_date"].strftime("%d/%m/%Y")
        table.add_row(str(num), task["name"], task["category"], du_date)
    
    console.print(table)

    if checkDetail:
        num = int(input("Task detail: "))
        
        print()
        
        task = tasks[num - 1]
        
        status = "❌Incompleted"
        if task["status"]:
            status = "✅ Completed"
        du_date = task["due_date"].strftime("%d/%m/%Y")
        created_date = task["created_date"].strftime("%d/%m/%Y, %H:%M:%S")

        print(f"Task name: {task['name']}")
        print(f"Description: {task['description']}")
        print(f"Category: {task['category']}")
        print(f"Status: {status}")
        print(f"Due Date: {du_date}")
        print(f"Created Date: {created_date}")
        
        print()
        
    return num
    
    
def Update_Task():
    
    # getTask = int(input("Enter Task Number: "))
    getTask = show_tasks()
    
    tasks = get_tasks()
    
    print()
    print("1. Change status")
    print("2. Change the name and description")
    print("3. Select the type of change")
    print()
    choice = input("Choose (1 | 2 | 3): ")
    
    task = tasks[getTask - 1]
    
    TaskTypeChange = ["name", "description", "category", "due_date", "status"]
    
    if choice == "1":
        task["status"] = not task["status"]
        print("Task status changed ✅")
            
    elif choice == "2":
        getName = input("Enter New Task Name: ")
        getDescription = input("Enter New Task Description: ")
        
        task["name"] = getName
        task["description"] = getDescription
        
    elif choice == "3":
        print()
        for index, taskKey in enumerate(TaskTypeChange, start=1):
            print(f"{index}. {taskKey.replace('_', ' ').title()}")
        print()
          
        choiceTaskChange = int(input("Enter select the type of change: "))
        
        if choiceTaskChange == 5:
            task["status"] = not task["status"]
            print("Task status changed ✅")
        else:
            NewTaskChange = input(f"Enter New {TaskTypeChange[choiceTaskChange-1].replace('_', ' ').title()}: ")
            tasks[getTask - 1][TaskTypeChange[choiceTaskChange-1]] = NewTaskChange
            print("Task status changed ✅")
    else:
        print("Wrong choice ❌")
        
    
    save_database(date_strftime_tasks(tasks))
    

def Delete_Task():
    show_tasks(False)
    
    getDeletedTasks = get_Deleted_tasks()
    tasks = get_tasks()
    
    GetDeleteTaskNum = int(input("Enter Delete Task Number: "))
    
    DeleteTask = tasks.pop(GetDeleteTaskNum - 1)
    getDeletedTasks.append(DeleteTask)
    
    save_Deletedtasks(date_strftime_tasks(getDeletedTasks))
    
    save_database(date_strftime_tasks(tasks))
    
    print("✅ Deleted Task")
    

def view_deleted():
    show_tasks(True, True)
    

def Mark_Completed():
    tasks = get_tasks()
    
    show_tasks(True, False)
    
    MarkCompleted = int(input("Enter Mark Completed Task: "))
    taskMark = tasks[MarkCompleted - 1]
    taskMark["status"] = True
    
    save_database(date_strftime_tasks(tasks))
    
    print()
    print("✅ Moves to Completed status.")