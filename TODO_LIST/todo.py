from tabulate import tabulate


class TODO():

    def __init__(self):
        with open("tasks.txt") as f:
            count = f.readlines()
            if len(count) > 0:
                self.taskcount = len(count)
            else:
                self.taskcount = 0

    def display_tasks(self):

        with open("tasks.txt") as f:
            tasks = f.readlines()
            items = [[i.strip()] for i in tasks]
            header = ["Tasks"]
            print(tabulate(items,header,tablefmt="grid"))


    def add_task(self):

        try:
            with open("tasks.txt","a") as file:
                task = input("Enter Task: ").title()
                file.write(f"{task}\n")
                self.taskcount += 1
        except FileNotFoundError:
            with open("tasks.txt","w") as file:
                task = input("Enter Task: ").title()
                file.write(f"{task}\n")
                self.taskcount += 1

    def remove_task(self):

        print("Here are your Tasks: ")
        self.display_tasks()
        task_to_remove = input("What task would you like to remove: ").title()

        with open("tasks.txt") as f :
            tasks = f.readlines()
            tasks.remove(f"{task_to_remove}\n")
            with open("tasks.txt","w") as file:
                for i in tasks:
                    file.write(i)
                self.taskcount -= 1
                print("Done")
        self.display_tasks()
            

    def edit_task(self):

        if self.taskcount == 0 :

            print("Hmmmm it seems like you have no tasks to edit would you like to add some? (y/n): ",end="")
            response = input().lower()
            if response == "y":
                self.add_task()
        else:

            print("Here are your Tasks: ")
            self.display_tasks()
            task_to_edit = input("What task would you like to edit: ").title()
            print(f"What would you like to change '{task_to_edit}' to ")
            new_task = input(": ")
            with open("tasks.txt") as f:
                list_of_tasks = f.read()
                print(list_of_tasks)
                

                with open('tasks.txt','w') as file:
                    file.write(list_of_tasks.replace(f"{task_to_edit}",f"{new_task}\n"))
                    print("Done")

            self.display_tasks()


            
