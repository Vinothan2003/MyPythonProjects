def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' is added to the TODO list.")


def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' is removed from TODO list")
    else:
        print(f"{task} is not found in the TODO list")


def view_task():
    print("\tTODO List")
    for task in to_do_list:
        print(task)


to_do_list = []

print("""
      Options 
    1.Add Task
    2.Remove Task
    3.View Task
    4.Quit
""")

while True:
    user_input = input("Enter Option 1 | 2 | 3 | 4 : ").strip()
    if user_input == "1":
        add_new_task = input("Enter a task :")
        add_task(add_new_task)
        print()
    elif user_input == "2":
        remove_task_list = input("Enter a task to remove :")
        remove_task(remove_task_list)
        print()

    elif user_input == "3":
        view_task()
        print()

    elif user_input == "4":
        print("Bye :)")
        break

    else:
        print("I don't understand!!")
