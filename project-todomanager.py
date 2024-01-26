import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk, ImageDraw
import tkinter.font as tkFont

def rounded_rectangle(size, radius, color):
    """Create an image of a rounded rectangle."""
    image = Image.new("RGBA", size, color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius, fill=color)
    return ImageTk.PhotoImage(image)

def button_click(action):
    print(f"Button clicked: {action}")

root = tk.Tk()
root.title("My To-Do List Manager")

# Function to add a task
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning(title="Warning!", message="You must enter a task.")

# Function to delete a task
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning(title="Warning!", message="You must select a task.")

# Function to load tasks
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
        listbox_tasks.delete(0, tk.END)
        for task in tasks:
            listbox_tasks.insert(tk.END, task)
            
        # Show a messagebox after loading tasks
        messagebox.showinfo("Loaded", "Tasks have been loaded successfully.")
        
    except FileNotFoundError:
        messagebox.showwarning(title="Warning!", message="Cannot find tasks.txt.")

# Function to save tasks
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

    # Show a messagebox after saving tasks
    messagebox.showinfo("Saved", "Tasks have been saved successfully.")
#listbox_tasks.configure(font=("Helvetica", 10),bg="#F5F5F5")

# Create GUI
frame_date = tk.Frame(root)
frame_date.pack(padx=(20, 20))

# Function to update the date and time label
def update_date_time():
    now = datetime.now()
    date_time_str = now.strftime("%A, %B %d, %Y %I:%M %p")
    date_label.config(text=date_time_str)
    root.after(1000, update_date_time)  # Schedule the update every 1000 milliseconds (1 second)

date_label = tk.Label(frame_date, font=("Cascadia Code", 12), fg = "blue")
date_label.pack(pady=15)
update_date_time()  # Start the date and time update loop

frame_tasks = tk.Frame(root)
frame_tasks.pack()

calendar = Calendar(frame_tasks, selectmode='day')
#calendar.pack(padx=(5, 5))
calendar.pack(pady=1)

label_after_calendar = tk.Label(frame_tasks, text="My to do list:", font=("Cascadia Code", 12), fg="blue")
label_after_calendar.pack(pady=10)


listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=35, font=("Cascadia Code", 12))
entry_task.pack(padx=(3, 5))
entry_task.pack(pady=5)

# Create rounded rectangles with different colors
rounded_button_img_add = rounded_rectangle((200, 35), 11, "#4CAF50")  # Green color
rounded_button_img_delete = rounded_rectangle((200, 35), 11, "#FF5733")  # Red color
rounded_button_img_load = rounded_rectangle((200, 35), 11, "#3498DB")  # Blue color
rounded_button_img_save = rounded_rectangle((200, 35), 11, "#F39C12")  # Yellow color

#1 Add button
button_add_task = tk.Label(root, text="Add task", image=rounded_button_img_add, compound="center", cursor="hand2", font=("Lucida Console", 11),fg="white")
button_add_task.photo = rounded_button_img_add
button_add_task.bind("<Button-1>", lambda event: add_task())
button_add_task.pack(pady=1)

#2 Delete button
button_delete_task = tk.Label(root, text="Delete task", image=rounded_button_img_delete, compound="center", cursor="hand2", font=("Lucida Console", 11),fg="white")
button_delete_task.photo = rounded_button_img_delete
button_delete_task.bind("<Button-1>", lambda event: delete_task())
button_delete_task.pack(pady=1)

#3 Load button
button_load_tasks = tk.Label(root, text="Load tasks", image=rounded_button_img_load, compound="center", cursor="hand2", font=("Lucida Console", 11),fg="white")
button_load_tasks.photo = rounded_button_img_load
button_load_tasks.bind("<Button-1>", lambda event: load_tasks())
button_load_tasks.pack(pady=1)

#4 Save button
button_save_tasks = tk.Label(root, text="Save tasks", image=rounded_button_img_save, compound="center", cursor="hand2", font=("Lucida Console", 11), fg="white")
button_save_tasks.photo = rounded_button_img_save
button_save_tasks.bind("<Button-1>", lambda event: save_tasks())
button_save_tasks.pack(pady=1)
button_save_tasks.pack(pady=(1, 20))


root.mainloop()