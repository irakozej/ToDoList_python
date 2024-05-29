array = []

def addTask(task):
    task = print("enter a task to add")
    array.append(task) 
    print(f"task '{task}' added to list")

def removeTask(task):
    task = print("enter a number for a task to remove")
    if task >= 0 and task < len(array):
        array.remove(task)
        print(f"task '{task}' removed from list")
    else:
        print("task not found")

def printTasks():
    print(array)

def updatetask(task, task2):
    task = print("enter a number for a task to update")
    if task >= 0 and task < len(array):
        task2 = input("enter a new task")
        array[task] = task2
        print(f"task '{task}' updated to '{task2}'")
    else:
        print("task not found")

def main():
    while True:
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Print tasks")
        print("4. Update a task")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            addTask()
        elif choice == 2:
            removeTask()
        elif choice == 3:
            printTasks()
        elif choice == 4:
            updatetask()
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()