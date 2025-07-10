import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip # Ensure pyperclip is installed for clipboard functionality

# function to generate a random password based on user input
def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError # If length is not a positive integer, raise an error

        characters = '' # Initialize an empty string for characters
        if include_letters.get(): characters += string.ascii_letters
        if include_numbers.get(): characters += string.digits
        if include_symbols.get(): characters += string.punctuation

        if not allow_repetition.get(): # If repetition is not allowed, use a set to ensure unique characters
            characters = ''.join(sorted(set(characters)))  # Remove duplicates

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type.")
            return
        # Check if the length is valid for the selected character set
        if not allow_repetition.get() and length > len(characters):
            messagebox.showerror("Error", "Length too long for selected character set without repetition.")
            return

        password_chars = []   # Initialize an empty list for password characters
        if include_letters.get(): password_chars.append(random.choice(string.ascii_letters))
        if include_numbers.get(): password_chars.append(random.choice(string.digits))
        if include_symbols.get(): password_chars.append(random.choice(string.punctuation))

        remaining = length - len(password_chars)
        if remaining < 0:
            messagebox.showerror("Error", "Length too short for selected options.")
            return

        if allow_repetition.get():
            password_chars += [random.choice(characters) for _ in range(remaining)]
        else:
            available_chars = list(set(characters) - set(password_chars))
            random.shuffle(available_chars)
            password_chars += available_chars[:remaining]

        random.shuffle(password_chars)
        result_var.set(''.join(password_chars))

    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive number.")

# function to copy the generated password to clipboard
def copy_to_clipboard():
    password = result_var.get() # Get the current password from the result variable
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

# GUI setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("420x480")
root.configure(bg="#ffffb7")
root.resizable(False, False)

# Fonts for the application
heading_font = ('Segoe UI', 20, 'bold')
label_font = ('Segoe UI', 12)
entry_font = ('Segoe UI', 12)
button_font = ('Segoe UI', 11)

# Header Label
tk.Label(root, text="Password Generator", font=heading_font, bg="#ffffb7").pack(pady=(20, 10))

# frame for input fields
frame = tk.Frame(root, bg="#ffffb7")
frame.pack()

# Length Input
tk.Label(frame, text="Length:", font=label_font, bg="#ffffb7").grid(row=0, column=0, sticky='w', padx=(20,5), pady=5)
length_var = tk.StringVar(value="12")
tk.Entry(frame, textvariable=length_var, font=entry_font, width=6, relief='solid').grid(row=0, column=1, sticky='w', pady=5)

# Checkbox Options
include_letters = tk.BooleanVar(value=True)
include_numbers = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=True)
allow_repetition = tk.BooleanVar(value=True)

checkbox_options = [   
    ("Include Letters", include_letters),
    ("Include Numbers", include_numbers),
    ("Include Symbols", include_symbols),
    ("Allow Repetition", allow_repetition)
]  # List of checkbox options

for i, (text, var) in enumerate(checkbox_options):  
    tk.Checkbutton(frame, text=text, variable=var, font=label_font,
                   bg="#ffffb7", anchor='w').grid(row=i+1, column=0, columnspan=2, sticky='w', padx=20)

# Result Entry
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=entry_font, width=32, justify='center',
         relief='solid', bd=1, fg="#444").pack(pady=20)

# Buttons for generating password and copying to clipboard
tk.Button(root, text="Generate Password", command=generate_password,
          font=button_font, bg="#6067AC", fg="white", activebackground="#4e5a99",
          relief="flat", width=30).pack(pady=(5, 5))

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,
          font=button_font, bg="#6067AC", fg="white", activebackground="#4e5a99",
          relief="flat", width=30).pack(pady=5)

# Footer Label
tk.Label(root, text="Made by Sakshi | 2025", font=('Segoe UI', 10), bg="#ffffb7").pack(side='bottom', pady=10)
root.mainloop()

