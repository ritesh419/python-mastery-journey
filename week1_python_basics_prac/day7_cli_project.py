# 🚀 DAY 7 – Build a Small CLI Project

def show_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = []

    while True:
        show_menu()
        print("\n")
        choice = input("Enter your choice: ")
        
        if choice =="1":
            print("\n")
            add_choice = input("Enter the task you have to add: ")
            tasks.append(add_choice)

        elif choice =="2":
            print("\n")
            if tasks == []:
                print("No tasks available\n")
            else:
                for number, item in enumerate(tasks, start=1):
                    print(f"{number}. {item}")

        elif choice =="3":
            print("\n")
            if not tasks:
                print("Task list is already empty")

            else:
                try: 
                    remove_task = int(input("Enter the task number that you want to be removed: "))

                    if remove_task <= 0 or remove_task > len(tasks):
                        raise IndexError
                    
                    del tasks[remove_task-1]
                    print("Task removed successfully")

                except ValueError:
                    print("Invalid input! Please enter a number.")

                except IndexError:
                    print("Invalid Task number")
              
        elif choice =="4":
            print("Exiting the program\n")
            break

        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()