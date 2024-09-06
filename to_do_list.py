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

def remove_task():
    view_tasks()
    try:
        task_number = int(input("\nEnter the number of the task to remove: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task '{removed_task.strip()}' removed from your to-do list!")
        else:
            print("Invalid task number!")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()