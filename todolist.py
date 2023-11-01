import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime


class TodoItem:
    def __init__(self, task, due_date):
        self.task = task
        self.due_date = due_date

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.todo_list = []

        # Eseménykezelés: gombnyomásra hozzáadás
        self.add_button = tk.Button(root, text="Hozzáadás", command=self.add_task)
        self.add_button.pack()

        # Lista megjelenítése
        self.listbox = tk.Listbox(root)
        self.listbox.pack()

        # Eseménykezelés: kijelölés törlése
        self.delete_button = tk.Button(root, text="Kijelölt törlése", command=self.delete_selected)
        self.delete_button.pack()

        # Eseménykezelés: lejárati dátum ellenőrzése
        self.check_button = tk.Button(root, text="Lejárati dátum ellenőrzése", command=self.check_due_dates)
        self.check_button.pack()

        # Fájl mentés és betöltés gomb
        self.save_button = tk.Button(root, text="Mentés", command=self.save_to_file)
        self.save_button.pack()
        self.load_button = tk.Button(root, text="Betöltés", command=self.load_from_file)
        self.load_button.pack()

        # Betöltjük a teendőket a szöveges fájlból
        self.load_from_file()

    def add_task(self):
        task = simpledialog.askstring("Hozzáadás", "Adja meg a teendőt:")
        due_date = simpledialog.askstring("Hozzáadás", "Adja meg a lejárati dátumot (YYYY-MM-DD):")

        if task and due_date:
            self.todo_list.append(TodoItem(task, due_date))
            self.listbox.insert(tk.END, task)

    def delete_selected(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.todo_list[index]
            self.listbox.delete(index)

    def check_due_dates(self):
        today = datetime.today().date()
        overdue_tasks = []
        for item in self.todo_list:
            due_date = datetime.strptime(item.due_date, "%Y-%m-%d").date()
            if due_date < today:
                overdue_tasks.append(item.task)

        if overdue_tasks:
            message = "Lejárt határidős teendők:\n" + "\n".join(overdue_tasks)
        else:
            message = "Nincs lejárt határidős teendő."

        messagebox.showinfo("Lejárati dátum ellenőrzés", message)

    def save_to_file(self):
        with open("todo.txt", "w") as file:
            for item in self.todo_list:
                file.write(f"{item.task}\t{item.due_date}\n")

    def load_from_file(self):
        try:
            with open("todo.txt", "r") as file:
                for line in file:
                    task, due_date = line.strip().split("\t")
                    self.todo_list.append(TodoItem(task, due_date))
                    self.listbox.insert(tk.END, task)
        except FileNotFoundError:
            messagebox.showinfo("Nincs fájl", "Nem található a teendők fájl. Új lista készült.")


