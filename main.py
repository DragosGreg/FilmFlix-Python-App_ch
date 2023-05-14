from readDatabase import readFilms
from insertDatabase import addFilms
from updateDatabase import updatefilmID
from deleteDatabase import deleteFilms


def menuOptions():
    options = 0 # flag variable

    while options not in ["1","2","3","4","5"]:
        print("\nHello, Wellcome to FilmFlix Database !\nPlease select one of the following options:\n\n1. To Print the Database.\n2. To Add a NeW Film to the Database.\n3. To Update a Field.\n4. To Delete a Field.\n5. To Exit.")
        # re-assign a new value to the options variable 
        options = input("\nEnter one of the options above: ")
        if options not in ["1","2","3","4","5"]:
            print(f"{options} is not a valid choice ")

    return options

mainProgram = True

while mainProgram:
    mainmenu = menuOptions()
    if mainmenu == "1":
        readFilms()
    elif mainmenu == "2":
        addFilms()
    elif mainmenu == "3":
        updatefilmID()
    elif mainmenu == "4":
        deleteFilms()
    else: # re-assign the value of main programe to False
        mainProgram = False

input("Press Enter to Exit")