from sqlConnect import *
from readDatabase import  readFilms
import time




def updatefilmID():
    # What field is ideal for updating a record in the songs table and why ?
    # FilmID     of the record to be updated
    idField = input("Enter the filmID of the Film to be updated: ")
    # Enter the name of the field(Title,Year Released,Rating,Duration,Genre)
    fieldName = input(
        "Which field would you like to update(Title,Year Released,Rating,Duration,Genre)? "
    ).title()
    # Enter the value for the field(Title,Year Released,Rating,Duration,Genre)
    newFieldValue = input(f"Enter the new value for the field: {fieldName} ")
    print(f"The new field value enterd is {newFieldValue}")
    # add single quotes arround the new field value
    # name  = Anna,  now name = " ' " + Anna + " ' "  = 'Anna'
    newFieldValue = "'" + newFieldValue + "'"
    print(f"The new field value enterd is {newFieldValue}")
    # Update the tblFilms table
    "UPDATE tblFilms SET(Title,Year Released,Rating,Duration,Genre) = newFieldValue(Dance/MJ/Pop) WHERE SongID = 1/2/3... "
    cursor.execute(
        f"UPDATE tblFilms SET {fieldName}  = {newFieldValue} WHERE FilmID = {idField}"
    )
    conn.commit()
    # returns the id of the film to be updated
    print(f"record {idField} Updated in the Films table")
    time.sleep(3)
    # call/invoke the readSongs from readData
    readFilms()

if __name__ == "__main__":
    updatefilmID()

