from sqlConnect import *
from readDatabase import readFilms
import time




def deleteFilms():
    idField = input("Enter the FilmID of the film you preffer to be deleted: ")
    cursor.execute(f"DELETE FROM tblFilms WHERE FilmID={idField}")
    print(f"Record {idField} deleted from the film table")
    time.sleep(3)
    readFilms()

if __name__ == "__main__":
    deleteFilms()