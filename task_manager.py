import csv
import os

TASKS_FILE = 'tasks.csv'

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            tasks = list(reader)
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'completed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

def list_tasks(tasks, only_pending=False):
    for task in tasks:
        if only_pending and task['completed'] == 'True':
            continue
        status = '✔' if task['completed'] == 'True' else '✘'
        print(f"[{status}] {task['id']}. {task['title']}")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    new_id = str(len(tasks) + 1)
    tasks.append({'id': new_id, 'title': title, 'completed': 'False'})
    save_tasks(tasks)
    print("Task added!")

def mark_complete(tasks):
    task_id = input("Enter task ID to mark as complete: ").strip()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = 'True'
            save_tasks(tasks)
            print("Task marked as complete!")
            return
    print("Task not found.")

def menu():
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. View all tasks")
        print("2. View pending tasks")
        print("3. Add task")
        print("4. Complete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            list_tasks(tasks, only_pending=True)
        elif choice == '3':
            add_task(tasks)
        elif choice == '4':
            mark_complete(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    menu()
