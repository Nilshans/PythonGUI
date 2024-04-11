import tkinter as tk
from tkinter import ttk
import subprocess

def run_script_and_update_label():
    # Run the bash script
    subprocess.run(["bash", "testScrape.sh"])

    # Update the label after 3 seconds
    root.after(3000, update_label_text)

def update_label_text():
    with open("rlsLog", "r") as file:
        lines = file.readlines()
        content = lines[2].strip()
        label1.config(text=content, font=("Arial", 12), fg="white")
#    label1.config(text="Label 1 Updated", font=("Arial", 12), fg="white")
    label2.config(text="Label 2 Updated", font=("Arial", 12), fg="white")
    label3.config(text="Label 3 Updated", font=("Arial", 12), fg="white")
    label4.config(text="Label 4 Updated", font=("Arial", 12), fg="white")

# Create the main window
root = tk.Tk()
root.title("Label Update App")

# Set the window size
root.geometry("400x800")

# Set background color to #273746
root.configure(bg="#273746")

# Create a button to update labels
style = ttk.Style()
style.configure('Green.TButton', foreground='white', background='green', font=('Arial', 12), bordercolor='black')
style.map('Green.TButton', foreground=[('pressed', 'white'), ('active', 'white')],
                           background=[('pressed', 'orange'), ('active', 'orange')])
update_button = ttk.Button(root, text="run_script_and_update_label", command=run_script_and_update_label, style='Green.TButton')
update_button.place(relx=0.5, rely=0.2, anchor="center")

# Create labels
label1 = tk.Label(root, text="Label 1", font=("Arial", 12), bg="#273746", fg="white")
label2 = tk.Label(root, text="Label 2", font=("Arial", 12), bg="#273746", fg="white")
label3 = tk.Label(root, text="Label 3", font=("Arial", 12), bg="#273746", fg="white")
label4 = tk.Label(root, text="Label 4", font=("Arial", 12), bg="#273746", fg="white")

# Center labels vertically and horizontally
label1.place(relx=0.5, rely=0.5, anchor="center")
label2.place(relx=0.5, rely=0.5, anchor="center", y=20)  # Adjusting y position for spacing
label3.place(relx=0.5, rely=0.5, anchor="center", y=40)  # Adjusting y position for spacing
label4.place(relx=0.5, rely=0.5, anchor="center", y=60)  # Adjusting y position for spacing

# Run the main event loop
root.mainloop()
