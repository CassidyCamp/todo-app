import sys

from .commands import (
    add_task,
    show_tasks,
    Update_Task,
    Delete_Task,
    view_deleted,
    Mark_Completed,
)


def main():
    while True:
        print()
        print("---menu----")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. View deleted task")
        print("6. Mark Completed")
        print("0. Exit")
        print()
        
        choice = input("Select option: ")
        print()
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            Update_Task()
        elif choice == "4":
            Delete_Task()
        elif choice == "5":
            view_deleted()
        elif choice == "6":
            Mark_Completed()
        elif choice == "0":
            sys.exit()
        else:
            print("Wrong choice ❌")
        