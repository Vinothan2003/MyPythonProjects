class InvalidOperationError(Exception):
    pass


class ToDoList:
    def __init__(self):
        self.todo_list = []

    def add_task(self, value):
        self.todo_list.append(value)
        print(f"Task '{value}' is Added to the ToDo List ")

    def mark_task(self, value):
        if value in self.todo_list:
            print(f"Task '{value}' is Marked!\nTask Completed")
        else:
            print(f"Task '{value}' is not in the ToDo List")

    def remove_task(self, value):
        if value in self.todo_list:
            self.todo_list.remove(value)
            print(f"Task '{value} is Removed'")
        else:
            print(f"Task '{value} is not in the ToDo List'")

    def view_task(self):
        if len(self.todo_list) == 0:
            print("Add some task in the ToDo List")
        else:
            print("---------ToDo List---------")
            for task in self.todo_list:
                print(task)


def main():
    todo = ToDoList()
    while True:
        try:
            print("""
            ------------ToDo List Form------------
            1.Add Task
            2.Mark Task
            3.Remove Task
            4.View Tasks
            5.Exit
            """)
            user_input = int(input("Enter 1 | 2 | 3 | 4 | 5 : "))
            if user_input == 1:
                task_add = input("Task Add > ")
                todo.add_task(task_add)
            elif user_input == 2:
                task_mark = input("Task Mark > ")
                todo.mark_task(task_mark)
            elif user_input == 3:
                task_remove = input("Task Remove > ")
                todo.remove_task(task_remove)
            elif user_input == 4:
                todo.view_task()
            elif user_input == 5:
                print("Bye:)")
                quit()
            else:
                print("Invalid Choice")

        except (InvalidOperationError, ValueError):
            print("Invalid Operation")


if __name__ == '__main__':
    main()
