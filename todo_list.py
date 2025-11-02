def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("\n No tasks yet. Add some!\n")
                return
            print("\n Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
            print()
    except FileNotFoundError:
        print("\n No tasks yet. Add some!\n")

def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        del tasks[task_num - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task removed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

while True:
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
