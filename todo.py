tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            num = int(input("Enter task number to remove: "))
            tasks.pop(num - 1)
            print("Task removed!")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
