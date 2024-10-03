import json
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load expenses from file
def load_expenses(filename='expenses.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses, filename='expenses.json'):
    with open(filename, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense():
    amount = amount_entry.get()
    date = date_entry.get() or datetime.now().strftime("%Y-%m-%d")
    selected_category = category_var.get()

    if not amount or not selected_category:
        messagebox.showerror("Input Error", "Please enter the amount and select a category.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")
        return

    expenses.append({'amount': amount, 'category': selected_category, 'date': date})
    save_expenses(expenses)
    messagebox.showinfo("Success", "Expense added successfully!")
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    category_var.set('')  # Clear the selected category

# Show summary in a popup window
def show_summary():
    summary_window = tk.Toplevel(root)
    summary_window.title("Expense Summary")

    tree = ttk.Treeview(summary_window, columns=('Amount', 'Category', 'Date'), show='headings')
    tree.heading('Amount', text='Amount')
    tree.heading('Category', text='Category')
    tree.heading('Date', text='Date')
    tree.pack(fill=tk.BOTH, expand=True)

    for expense in expenses:
        tree.insert('', tk.END, values=(f"${expense['amount']:.2f}", expense['category'], expense['date']))

    summary_window.geometry('400x300')
    summary_window.grab_set()

# Plot expenses by category
def plot_expenses():
    categories = {}
    for expense in expenses:
        categories[expense['category']] = categories.get(expense['category'], 0) + expense['amount']

    if categories:
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=140)
        ax.set_title("Expense Distribution by Category")

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)
    else:
        messagebox.showinfo("No Data", "No expenses to plot.")

# Main GUI setup
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("400x400")

expenses = load_expenses()

# GUI layout
tk.Label(root, text="Add New Expense").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Amount:").grid(row=1, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

# Category Section with Checkboxes
tk.Label(root, text="Category:").grid(row=2, column=0, padx=10, pady=5)

category_var = tk.StringVar()
category_frame = tk.Frame(root)
category_frame.grid(row=2, column=1)

tk.Radiobutton(category_frame, text="Food", variable=category_var, value="Food").pack(anchor='w')
tk.Radiobutton(category_frame, text="Transport", variable=category_var, value="Transport").pack(anchor='w')
tk.Radiobutton(category_frame, text="Entertainment", variable=category_var, value="Entertainment").pack(anchor='w')

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Summary and Plot Buttons
tk.Button(root, text="Show Summary", command=show_summary).grid(row=5, column=0, columnspan=2, padx=10, pady=5)
tk.Button(root, text="Show Pie Chart", command=plot_expenses).grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Allow resizing and grid auto-adjustment
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(7, weight=1)

# Start the GUI loop
root.mainloop()
