import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f4f7")

        # Title
        self.label_title = tk.Label(self.root, text="Secure Password Generator", font=("Helvetica", 16, "bold"), bg="#007bff", fg="white")
        self.label_title.pack(fill=tk.X, pady=10)

        # Password Length Input
        self.label_length = tk.Label(self.root, text="Password Length:", bg="#f0f4f7", font=("Arial", 12))
        self.label_length.pack(pady=5)
        self.entry_length = tk.Entry(self.root, width=5, font=("Arial", 12))
        self.entry_length.pack()

        # Checkboxes for criteria
        self.use_uppercase = tk.BooleanVar()
        self.use_numbers = tk.BooleanVar()
        self.use_symbols = tk.BooleanVar()

        self.checkbox_uppercase = tk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.use_uppercase, bg="#f0f4f7", font=("Arial", 12))
        self.checkbox_uppercase.pack(anchor=tk.W, padx=20)

        self.checkbox_numbers = tk.Checkbutton(self.root, text="Include Numbers", variable=self.use_numbers, bg="#f0f4f7", font=("Arial", 12))
        self.checkbox_numbers.pack(anchor=tk.W, padx=20)

        self.checkbox_symbols = tk.Checkbutton(self.root, text="Include Symbols", variable=self.use_symbols, bg="#f0f4f7", font=("Arial", 12))
        self.checkbox_symbols.pack(anchor=tk.W, padx=20)

        # Generate Password Button
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password, font=("Arial", 12), bg="#28a745", fg="white")
        self.generate_button.pack(pady=10)

        # Password Display
        self.entry_password = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.entry_password.pack(pady=5)

        # Copy to Clipboard Button
        self.copy_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Arial", 12), bg="#007bff", fg="white")
        self.copy_button.pack(pady=10)

    def generate_password(self):
        length = int(self.entry_length.get())
        use_uppercase = self.use_uppercase.get()
        use_numbers = self.use_numbers.get()
        use_symbols = self.use_symbols.get()

        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(0, password)

    def copy_to_clipboard(self):
        password = self.entry_password.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Error", "No password to copy!")

# Main
root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
