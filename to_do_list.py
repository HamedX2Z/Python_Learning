def display_menu():
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if tasks:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("\nYour To-Do List is empty!")
    except FileNotFoundError:
        print("\nYour To-Do List is empty!")

def add_task():
    task = input("\nEnter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added to your to-do list!")