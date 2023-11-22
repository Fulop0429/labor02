def save_to_file(todo_list, filename="todo.txt"):
    with open(filename, "w") as file:
        for item in todo_list:
            file.write(f"{item.task}\t{item.due_date}\n")

def load_from_file(todo_list, filename="todo.txt"):
    from todolist import TodoItem
    try:
        todo_list.clear()
        with open(filename, "r") as file:
            for line in file:
                task, due_date = line.strip().split("\t")
                todo_list.append(TodoItem(task, due_date))
    except FileNotFoundError:
        print("Nem található a teendők fájl. Új lista készült.")

