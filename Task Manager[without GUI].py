import os

# Load tasks from file
def load_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip().split(",") for line in file]
    return []

# Save tasks to file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        file.writelines([f"{t[0]},{t[1]}\n" for t in tasks])

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task[0]} ({'Complete' if task[1] == 'True' else 'Incomplete'})")

# Add new task
def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append([title, "False"])

# Edit task
def edit_task(tasks):
    display_tasks(tasks)
    idx = int(input("Task number to edit: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx][0] = input("New title: ").strip()

# Mark task as complete
def complete_task(tasks):
    display_tasks(tasks)
    idx = int(input("Task number to complete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx][1] = "True"

# Delete task
def delete_task(tasks):
    display_tasks(tasks)
    idx = int(input("Task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)

# Task manager menu
def task_manager():
    tasks = load_tasks()
    actions = {"1": display_tasks, "2": add_task, "3": edit_task, "4": complete_task, "5": delete_task}

    while True:
        print("\n1. View Tasks \n2. Add Task \n3. Edit Task \n4. Complete Task \n5. Delete Task  \n6. Exit")
        choice = input("Choose: ")
        if choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break
        if choice in actions:
            actions[choice](tasks)

task_manager()
