import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Fixed Size Calculator")
root.geometry("300x400")  # Set the fixed size

entry = tk.Entry(root, font=("Helvetica", 20))
entry.pack(fill=tk.BOTH, expand=True)

buttons_frame = tk.Frame(root)
buttons_frame.pack(fill=tk.BOTH, expand=True)

button_symbols = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in button_symbols:
    button = tk.Button(buttons_frame, text=text, font=("Helvetica", 20), padx=20, pady=20)
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", on_button_click)

# Configure grid layout to expand properly
for i in range(5):
    buttons_frame.grid_rowconfigure(i, weight=1)
    buttons_frame.grid_columnconfigure(i, weight=1)

root.mainloop()