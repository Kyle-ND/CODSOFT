from todo import TODO
import pyfiglet
import os
from time import sleep 

def main():
    Lis = TODO()
    running = True
    f = pyfiglet.figlet_format("TODO-LIST", font="slant")
    print(f)

    while running:

        print(f"Number of tasks: {Lis.taskcount}")
        functions()
        response = input(": ")

        if response == "1":
            Lis.add_task()
            os.system("cls")

        elif response == "2":
            os.system("cls")
            Lis.display_tasks()
            sleep(2)

        elif response == "3":
            os.system("cls")
            Lis.edit_task()
            os.system("cls")

        elif response == "4":
            running = False
            os.system("cls")
            
        else:
            print("I didn't quite get that :(")
            os.system("cls")

    f = pyfiglet.figlet_format("GOODBYE :)", font="slant")
    print(f)


def functions():
    print("""
----------   ----------
1. ADD TASKS
2. VIEW TASKS
3. REMOVE TASKS
4. Quit
----------    ----------            
          """)

main()