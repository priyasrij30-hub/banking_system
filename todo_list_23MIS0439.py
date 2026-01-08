tasks = []

while True:
    print("1.Add  2.View  3.Exit")
    choice = input("Choice: ")

    if choice == "1":
        tasks.append(input("Enter task: "))
    elif choice == "2":
        print("Tasks:", tasks)
    elif choice == "3":
        break
    else:
        print("Invalid choice")
