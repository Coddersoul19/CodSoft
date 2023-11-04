import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

app = tk.Tk()
app.title("Simple Calculator")

entry = tk.Entry(app, font=("Helvetica", 16))
entry.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(app)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row, col = 1, 0

for button in buttons:
    button_obj = tk.Button(button_frame, text=button, font=("Helvetica", 16), height=2, width=5)
    button_obj.grid(row=row, column=col)
    button_obj.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

app.mainloop()
