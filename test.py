import tkinter as tk
from tkinter import messagebox

def greet():
    name = name_entry.get()
    messagebox.showinfo("Greetings", f"Hello, {name}!")

# Create the main window
root = tk.Tk()
root.title("Greeting App")

# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack()

# Create an entry field
name_entry = tk.Entry(root)
name_entry.pack()

# Create a button
greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack()

# Run the main event loop
root.mainloop()
