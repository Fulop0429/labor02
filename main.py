import tkinter as tk
from todolist import TodoListApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()