# task 1

from datetime import datetime
import datetime
class Task:
    def __init__(self, title, description, due_datetime=None, completed=False):
        self.title = title
        self.description = description
        self.due_datetime = due_datetime
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Not Done"
            due_datetime = task.due_datetime.strftime("%Y-%m-%d %H:%M") if task.due_datetime else "No Due Date"
            print(f"{i}. {task.title} - {task.description} [Due: {due_datetime}] [{status}]")

    def search_tasks(self, query):
        results = [task for task in self.tasks if query.lower() in task.title.lower()]
        return results

    def update_task_status(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            print("Task status updated successfully.")
        else:
            print("Invalid index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid index.")

    def set_due_datetime(self, index, due_datetime):
        if 0 <= index < len(self.tasks):
            try:
                self.tasks[index].due_datetime = datetime.strptime(due_datetime, "%Y-%m-%d %H:%M")
                print("Due date and time set successfully.")
            except ValueError:
                print("Invalid date and time format. Please use YYYY-MM-DD HH:MM.")
        else:
            print("Invalid index.")

def run_todo_list():
    todo_list = ToDoList()

    while True:
        print("\n Welcome to To-Do List Application")
        print("1. Add Task\n2. View Tasks\n3. Search Tasks\n4. Update Task Status\n5. Set Due Date and Time\n6. Delete Task\nType 'exit' to Exit")

        choice = input("Enter your choice: ").lower()

        if choice == "1":
            todo_list.add_task(Task(input("Task Title: "), input("Task Description: ")))
            print("Task added successfully!")

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            query = input("Enter task title to search: ")
            results = todo_list.search_tasks(query)
            print("Search Results:" if results else "No matching tasks found.")
            [print(f"{i}. {task.title} - {task.description}") for i, task in enumerate(results, start=1)]

        elif choice == "4":
            todo_list.view_tasks()
            try:
                index = int(input("Enter index of the task to update status: ")) - 1
                todo_list.update_task_status(index)
            except (ValueError, IndexError):
                print("Invalid input or index.")

        elif choice == "5":
            todo_list.view_tasks()
            try:
                index = int(input("Enter index of the task to set due date and time: ")) - 1
                due_datetime = input("Enter due date and time (YYYY-MM-DD HH:MM): ")
                todo_list.set_due_datetime(index, due_datetime)
            except (ValueError, IndexError):
                print("Invalid input or index.")

        elif choice == "6":
            todo_list.view_tasks()
            try:
                index = int(input("Enter index of the task to delete: ")) - 1
                todo_list.delete_task(index)
                print("Task deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid input or index.")

        elif choice == "exit":
            print(".............Closing To-Do List Application............")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


run_todo_list()
