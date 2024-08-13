import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        # Create a frame for the listbox and scrollbar
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Create a listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT)

        # Create a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Attach the scrollbar to the listbox
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry box for new tasks
        self.task_entry = tk.Entry(self.master, width=52)
        self.task_entry.pack(pady=10)

        # Add task button
        self.add_task_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Remove task button
        self.remove_task_button = tk.Button(self.master, text="Remove Selected Task", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Clear the entry box
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()