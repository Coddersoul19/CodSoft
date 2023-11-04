import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task = tasks.curselection()[0]
        tasks.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

app = tk.Tk()
app.title("To-Do List")
app.geometry("400x300")

frame = tk.Frame(app)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30, font=("Helvetica", 14))
entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(frame, text="Add Task", command=add_task, font=("Helvetica", 12), bg="green", fg="white")
add_button.grid(row=0, column=1, padx=10, pady=10)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task, font=("Helvetica", 12), bg="red", fg="white")
delete_button.grid(row=0, column=2, padx=10, pady=10)

tasks = tk.Listbox(app, selectbackground="yellow", font=("Helvetica", 14))
tasks.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

app.mainloop()
