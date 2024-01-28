import tkinter as tk

def on_click(button_value):
    current_text = entry_var.get()
    
    if button_value == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + str(button_value))

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying the current input and result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)

# Buttons for digits and operations
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 14),
                       command=lambda t=text: on_click(t))
    button.grid(row=row, column=column)

# Run the main loop
root.mainloop()
