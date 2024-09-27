import tkinter as tk
from tkinter import ttk

def update_labels():
    label1.config(text="Label 1 Updated", font=("Arial", 12), fg="white")
    label2.config(text="Label 2 Updated", font=("Arial", 12), fg="white")
    label3.config(text="Label 3 Updated", font=("Arial", 12), fg="white")
    label4.config(text="Label 4 Updated", font=("Arial", 12), fg="white")

# Create the main window
root = tk.Tk()
root.title("Label Update App")

# Set the window size
root.geometry("400x800")

# Set background color to blue
root.configure(bg="#5D6D7E")

# Create labels
label1 = tk.Label(root, text="Label 1", font=("Arial", 12), bg="#273746", fg="white")
label2 = tk.Label(root, text="Label 2", font=("Arial", 12), bg="#273746", fg="white")
label3 = tk.Label(root, text="Label 3", font=("Arial", 12), bg="#273746", fg="white")
label4 = tk.Label(root, text="Label 4", font=("Arial", 12), bg="#273746", fg="white")

# Center labels vertically
label1.grid(row=0, column=0, pady=(200, 10), sticky="ew")
label2.grid(row=1, column=0, pady=10, sticky="ew")
label3.grid(row=2, column=0, pady=10, sticky="ew")
label4.grid(row=3, column=0, pady=10, sticky="ew")

# Create a button to update labels
style = ttk.Style()
style.configure('Green.TButton', foreground='white', background='green', font=('Arial', 12), bordercolor='black')
style.map('Green.TButton', foreground=[('pressed', 'white'), ('active', 'white')],
                           background=[('pressed', 'orange'), ('active', 'orange')])
update_button = ttk.Button(root, text="Update Labels", command=update_labels, style='Green.TButton')
update_button.grid(row=4, column=0, pady=10, sticky="ew")

# Run the main event loop
root.mainloop()
