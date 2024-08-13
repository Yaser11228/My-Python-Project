import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Form")

        # Create a frame for the form
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Username label and entry
        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)

        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password label and entry
        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)

        self.password_entry = tk.Entry(self.frame, show='*')  # Hide password input
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Login button
        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Simple validation check (you can modify this logic)
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()