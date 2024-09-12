import os

# Function to display tasks
def display_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} - {'Complete' if task['completed'] else 'Incomplete'}")
    if not tasks:
        print("No tasks available.")

# Function to handle common task operations
def task_action(tasks, action):
    display_tasks(tasks)
    task_num = int(input(f"Enter task number to {action}: ")) - 1
    return task_num if 0 <= task_num < len(tasks) else None

# Function to add, edit, delete, or mark task as complete
def add_task(tasks):
    tasks.append({"title": input("Enter task title: "), "completed": False})

def edit_task(tasks):
    task_num = task_action(tasks, "edit")
    if task_num is not None:
        tasks[task_num]['title'] = input("Enter new task title: ")

def delete_task(tasks):
    task_num = task_action(tasks, "delete")
    if task_num is not None:
        tasks.pop(task_num)

def mark_task_complete(tasks):
    task_num = task_action(tasks, "mark as complete")
    if task_num is not None:
        tasks[task_num]['completed'] = True

# Function to save and load tasks from a file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as f:
        f.writelines([f"{t['title']},{t['completed']}\n" for t in tasks])

def load_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return [{"title": title, "completed": completed == "True"} for title, completed in (line.strip().split(",") for line in f)]
    return []

# Main function
def main():
    tasks = load_tasks()
    actions = {
        '1': ("View Tasks", display_tasks),
        '2': ("Add Task", add_task),
        '3': ("Edit Task", edit_task),
        '4': ("Delete Task", delete_task),
        '5': ("Mark Task Complete", mark_task_complete),
    }

    while True:
        print("\nTo-Do List Menu:")
        for num, (label, _) in actions.items():
            print(f"{num}. {label}")
        print("6. Save and Exit")

        choice = input("Choose an option: ")
        if choice == '6':
            save_tasks(tasks)
            print("Tasks saved! Goodbye!")
            break
        elif choice in actions:
            actions[choice][1](tasks)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
