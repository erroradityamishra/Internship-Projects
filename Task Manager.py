import tkinter as tk
from tkinter import messagebox
import os

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("450x400")
        self.root.configure(bg="#f0f4f7")  # Light background color

        # Load tasks
        self.tasks = self.load_tasks()

        # Create the title label
        self.label_title = tk.Label(self.root, text="Task Manager", font=("Helvetica", 18, "bold"), bg="#007bff", fg="white", pady=10)
        self.label_title.pack(fill="x")

        # Task list display frame
        self.tasks_frame = tk.Frame(self.root, bg="#f0f4f7")
        self.tasks_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.tasks_frame, font=("Arial", 12), height=10, selectbackground="#007bff", selectforeground="white")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for listbox
        self.scrollbar = tk.Scrollbar(self.tasks_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure listbox and scrollbar
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry for adding new tasks
        self.entry_task = tk.Entry(self.root, font=("Arial", 14), width=30, bd=2, relief=tk.SUNKEN)
        self.entry_task.pack(pady=10)

        # Button frame for better layout
        self.button_frame = tk.Frame(self.root, bg="#f0f4f7")
        self.button_frame.pack(fill=tk.X, pady=10)

        # Add Task Button
        self.add_button = tk.Button(self.button_frame, text="Add Task", font=("Arial", 12), bg="#28a745", fg="white", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        # Mark as Complete Button
        self.mark_button = tk.Button(self.button_frame, text="Mark as Complete", font=("Arial", 12), bg="#ffc107", fg="black", command=self.mark_task_complete)
        self.mark_button.grid(row=0, column=1, padx=5)

        # Delete Task Button
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", font=("Arial", 12), bg="#dc3545", fg="white", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Load the tasks into the listbox
        self.refresh_task_list()

    # Load tasks from file
    def load_tasks(self, filename="tasks.txt"):
        tasks = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    title, completed = line.strip().split(",")
                    tasks.append({"title": title, "completed": completed == "True"})
        return tasks

    # Save tasks to file
    def save_tasks(self, filename="tasks.txt"):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task['title']},{task['completed']}\n")

    # Refresh task list in the listbox
    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task['title']
            if task['completed']:
                task_text += " (Complete)"
                self.task_listbox.insert(tk.END, task_text)
                self.task_listbox.itemconfig(tk.END, {'fg': 'green'})  # Green color for completed tasks
            else:
                self.task_listbox.insert(tk.END, task_text)

    # Add a new task
    def add_task(self):
        task_title = self.entry_task.get().strip()
        if task_title == "":
            messagebox.showwarning("Input Error", "Please enter a task title.")
        else:
            self.tasks.append({"title": task_title, "completed": False})
            self.entry_task.delete(0, tk.END)
            self.refresh_task_list()
            self.save_tasks()

    # Mark selected task as complete
    def mark_task_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")
        else:
            index = selected_task_index[0]
            self.tasks[index]['completed'] = True
            self.refresh_task_list()
            self.save_tasks()

    # Delete selected task
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
        else:
            index = selected_task_index[0]
            del self.tasks[index]
            self.refresh_task_list()
            self.save_tasks()

# Create the main window
root = tk.Tk()
app = TaskManagerApp(root)

# Start the Tkinter event loop
root.mainloop()
