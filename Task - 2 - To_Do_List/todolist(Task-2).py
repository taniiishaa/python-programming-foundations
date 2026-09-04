# todo.py
# A simple CLI To-Do List Application (Persistent)

# File to store tasks
TASK_FILE = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Function to display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to add a new task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main Program
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
