from readDatabase import readFilms
from printDatabase import *


def menuOptions():
    options = 0 # flag variable

    while options not in ["1","2","3","4","5"]:
        print("\nHello, Wellcome to FilmFlix Database !\nPlease select one of the following options:\n\n1. Print details of all films.\n2. Print all films of a particular genre.\n3. Print all films of a particular year .\n4. Print all films of a particular rating \n5. To Exit.")
        # re-assign a new value to the options variable 
        options = input("\nEnter one of the options above: \n")
        if options not in ["1","2","3","4","5"]:
            print(f"{options} is not a valid choice ")

    return options

mainProgram = True

while mainProgram:
    mainmenu = menuOptions()
    if mainmenu == "1":
        readFilms()
    elif mainmenu == "2":
        readFilms2()
    elif mainmenu == "3":
        readFilms3()
    elif mainmenu == "4":
        readFilms4()
    else: # re-assign the value of main programe to False
        mainProgram = False

input("Press Enter to Exit")