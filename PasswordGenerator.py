import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.use_uppercase = tk.BooleanVar()
        self.use_lowercase = tk.BooleanVar()
        self.use_digits = tk.BooleanVar()
        self.use_special = tk.BooleanVar()

        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=self.use_uppercase)
        self.lowercase_check = tk.Checkbutton(root, text="Include Lowercase", variable=self.use_lowercase)
        self.digits_check = tk.Checkbutton(root, text="Include Digits", variable=self.use_digits)
        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.use_special)

        self.uppercase_check.pack()
        self.lowercase_check.pack()
        self.digits_check.pack()
        self.special_check.pack()

        #Generate button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_text = tk.Text(root, height=3, width=50)
        self.password_text.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
            return

        character_sets = []
        if self.use_uppercase.get():
            character_sets.append(string.ascii_uppercase)
        if self.use_lowercase.get():
            character_sets.append(string.ascii_lowercase)
        if self.use_digits.get():
            character_sets.append(string.digits)
        if self.use_special.get():
            character_sets.append(string.punctuation)
        
        if not character_sets:
            messagebox.showerror("Invalid input", "At least one character type must be selected.")
            return

        all_characters = ''.join(character_sets)
        password = ''.join(random.choice(all_characters) for _ in range(length))
        
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(tk.END, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
