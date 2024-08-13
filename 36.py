# Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and decrement buttons.
import tkinter as tk


class CounterApp:
    def __init__(self,root):
        self.count = 0
        self.label = tk.Label(root, text=str(self.count))
        self.label.pack()
        increment_button = tk.Button(root, text="Increment", command=self.increment)
        increment_button.pack()
        decrement_button = tk.Button(root, text="Decrement", command=self.decrement)
        decrement_button.pack()

    def increment(self):
        self.count += 1
        self.label.config(text=str(self.count))

    def decrement(self):
        self.count -= 1
        self.label.config(text=str(self.count))


root = tk.Tk()
app = CounterApp(root)
root.mainloop()


