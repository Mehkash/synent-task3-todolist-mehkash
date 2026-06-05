tasks = []

while True:
    print("\n📋 ===== TO-DO LIST =====")
    print("1. 👀 View Tasks")
    print("2. ➕ Add Task")
    print("3. ✅ Mark Task as Completed")
    print("4. ❌ Delete Task")
    print("5. 🚪 Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                if task["completed"]:
                    status = "✅"
                else:
                    status = "❌"
                print(f"{i}. {status} {task['name']}")

    elif choice == "2":
        task_name = input("Enter task: ")
        tasks.append({
            "name": task_name,
            "completed": False
        })
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                if task["completed"]:
                    status = "✅"
                else:
                    status = "❌"
                print(f"{i}. {status} {task['name']}")

            try:
                task_num = int(input("\nEnter task number to mark as completed: "))

                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print("✅ Task marked as completed!")
                else:
                    print("⚠️ Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{i}. {status} {task['name']}")

            try:
                task_num = int(input("\nEnter task number to delete: "))

                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"🗑️ '{removed['name']}' deleted successfully!")
                else:
                    print("⚠️ Invalid task number.")

            except ValueError:
                print("⚠️ Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please select between 1 and 5.")