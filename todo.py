tasks = []


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Complete")
    print("5. Exit")




def add_task():
    task = input("Enter task: ").strip()
    
    if task:
        tasks.append(task)
        save_tasks()
        print("Task added!")
    else:
        print("Task cannot be empty")



def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")



def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks()
            print(f"Task '{removed}' deleted!")
        else:
            print("Invalid task number")
    except:
        print("Invalid input")

def mark_complete():
    view_tasks()
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num-1] += " ✔"
        save_tasks()
        print("Task marked as completed!")
    except:
        print("Invalid input")



load_tasks()

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_complete()
    elif choice=="5":
        break
    else:
        print("Invalid choice, try again")
