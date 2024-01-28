import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
import random
import string

def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        
        result_var.set(generated_password)
    except ValueError as e:
        result_var.set("Error: " + str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and Entry for specifying password length
length_label = Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Display the generated password
result_var = StringVar()
result_label = Label(root, textvariable=result_var, font=("Courier", 14), wraplength=400)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
