import tkinter as tk
from tkinter import Entry, StringVar
import random
import string

def generate_password(length, complexity):
    characters = ""
    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    username = username_var.get()
    length = int(length_var.get())
    complexity = complexity_var.get()
    password = generate_password(length, complexity)
    
    result_text = f"Username: {username}\nPassword: {password}"
    result_var.set(result_text)

app = tk.Tk()
app.title("Password Generator")
app.geometry("400x350")

frame = tk.Frame(app)
frame.pack(pady=10)

username_label = tk.Label(frame, text="Username:", font=("Arial", 12))
username_label.grid(row=0, column=0, padx=10, pady=5)

username_var = StringVar()
username_entry = Entry(frame, textvariable=username_var, font=("Arial", 12))
username_entry.grid(row=0, column=1, padx=10, pady=5)

length_label = tk.Label(frame, text="Password Length:", font=("Arial", 12))
length_label.grid(row=1, column=0, padx=10, pady=5)

length_var = StringVar()
length_entry = Entry(frame, textvariable=length_var, font=("Arial", 12))
length_entry.grid(row=1, column=1, padx=10, pady=5)

complexity_label = tk.Label(frame, text="Complexity:", font=("Arial", 12))
complexity_label.grid(row=2, column=0, padx=10, pady=5)

complexity_options = ["Low", "Medium", "High"]
complexity_var = StringVar()
complexity_var.set(complexity_options[0])
complexity_menu = tk.OptionMenu(frame, complexity_var, *complexity_options)
complexity_menu.grid(row=2, column=1, padx=10, pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate, font=("Arial", 12), bg="blue", fg="white")
generate_button.grid(row=3, columnspan=2, pady=10)

result_var = StringVar()
result_label = tk.Label(app, textvariable=result_var, font=("Arial", 14), relief="ridge")
result_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

app.mainloop()

