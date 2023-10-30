import tkinter as tk
from datetime import datetime  # datetime modul importálása


class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Hozzáadás", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.remove_button = tk.Button(self.root, text="Törlés", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=10, pady=10)

        self.task_count_label = tk.Label(self.root, text="Feladatok száma: 0")
        self.task_count_label.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            now = datetime.now()
            task_with_timestamp = f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {task}"
            self.tasks.append(task_with_timestamp)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
            self.update_task_count()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            del self.tasks[selected_index]
            self.update_task_listbox()
            self.update_task_count()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def update_task_count(self):
        count = len(self.tasks)
        self.task_count_label.config(text="Feladatok száma: {}".format(count))


def main():
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()


if __name__ == "__main__":
    main()