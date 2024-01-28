import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update_task():
    selected_task_index = listbox.curselection()
    updated_task = entry.get()
    if selected_task_index and updated_task:
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, updated_task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task and enter an update.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Entry widget for entering tasks
entry = tk.Entry(root, width=40, font=("Helvetica", 14))
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Buttons for adding, updating, and removing tasks
add_button = tk.Button(root, text="Add", command=add_task, font=("Helvetica", 12))
add_button.grid(row=0, column=2, padx=5, pady=10)

update_button = tk.Button(root, text="Update", command=update_task, font=("Helvetica", 12))
update_button.grid(row=0, column=3, padx=5, pady=10)

remove_button = tk.Button(root, text="Remove", command=remove_task, font=("Helvetica", 12))
remove_button.grid(row=0, column=4, padx=5, pady=10)

# Listbox for displaying tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10, font=("Helvetica", 12))
listbox.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# Run the main loop
root.mainloop()
