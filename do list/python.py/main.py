# Simple To-Do List Application

tasks = []  # List to store tasks

# Function to add a new task
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks to display!")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} - {status}")

# Function to mark a task as completed
def mark_completed(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed!")
    else:
        print("Invalid task number!")

# Function to delete a task
def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' deleted successfully!")
    else:
        print("Invalid task number!")

# Function to display menu
def menu():
    print("\nTo-Do List Application")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

# Main function to run the program
def main():
    while True:
        menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            task = input("Enter the new task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_completed(task_number)
        elif choice == "4":
            view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
