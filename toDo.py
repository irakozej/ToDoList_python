array = []

def addTask(task):
    task = input("enter a task to add: \n" )
    array.append(task) 
    print(f"task '{task}' added to list")


def addTask():
    task = input("Enter a task to add: \n")
    array.append(task)
    print(f"Task '{task}' added to list")


def removeTask(task):
    task = input("enter a number for a task to remove: \n")
    if task >= 0 and task < len(array):
        array.remove(task)
        print(f"task '{task}' removed from list")
    else:
        print("task not found")

def printTasks():
    print(array)

def updatetask():
    task = int(input("enter a number for a task to update: \n"))
    if task >= 0 and task < len(array):
        task2 = input("enter a new task: ")
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
        choice = int(input("Enter your choice: \n"))
        if choice == 1:
            addTask()
        elif choice == 2:
            removeTask()
        elif choice == 3:
            printTasks()
        elif choice == 4:
            updatetask()
        elif choice == 5:
            print("thanks for interacting with the program 🤝")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()