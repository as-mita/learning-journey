import json
import os

TASK_FILE = "tasks.json"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(TASK_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description):
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        self.save_tasks()
        print("✓ Task added!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, 1):
            status = "✔" if task["completed"] else "✗"
            print(f"{i}. {task['description']} [{status}]")

    def complete_task(self, task_num):
        try:
            self.tasks[task_num - 1]["completed"] = True
            self.save_tasks()
            print("✓ Task marked as completed!")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_num):
        try:
            self.tasks.pop(task_num - 1)
            self.save_tasks()
            print("✓ Task deleted!")
        except IndexError:
            print("Invalid task number.")


def menu():
    manager = TaskManager()
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter task: ")
            manager.add_task(desc)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            num = int(input("Task number to complete: "))
            manager.complete_task(num)

        elif choice == "4":
            num = int(input("Task number to delete: "))
            manager.delete_task(num)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
