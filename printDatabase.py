from sqlConnect import *
from readDatabase import  readFilms
import time

# def readFilms2():
#     cursor.execute("SELECT * FROM tblFilms WHERE genre='Comedy'") 
#     row = cursor.fetchall() 
#     for record in row:
#         print(record)

# if __name__ == "__main__":
#     readFilms2()
# ######################################################################
# def readFilms3():
#     cursor.execute("SELECT * FROM tblFilms WHERE yearReleased>2016") 
#     row = cursor.fetchall() 
#     for record in row:
#         print(record)

# if __name__ == "__main__":
#     readFilms3()
# ######################################################################
# def readFilms4():
#     cursor.execute("SELECT * FROM tblFilms WHERE  rating='PG' ORDER BY title ASC") 
#     row = cursor.fetchall() 
#     for record in row:
#         print(record)

# if __name__ == "__main__":
#     readFilms4()

#######################################################################


# def readFilms5():
#     fieldName = input("Which field would you like to print(genre,yearReleased,rating) ?")
#     printValue = input("Select a particuloar value for your choosen field: ")
#     print("Print Value", printValue)
#     printValue = "'" + printValue + "'"
#     print("User amended input", printValue)


#     try:
#         cursor.execute("SELECT * FROM tblFilms WHERE" + fieldName + "=" + printValue)
#         conn.commit()
#         row = cursor.fetchall()
#         for record in row:
#             print(record)
#     except:
#         print("FIeld" + printValue + "does not exist")
#     finally:
#         conn.close()


################################################################################

def printfilmID():
        # Enter the name of the field(Title,Year Released,Rating,Duration,Genre)
    fieldName = input(
       "Which field would you like to print(genre,yearReleased,rating) ? "
    )
    # Enter the value for the field(Title,Year Released,Rating,Duration,Genre)
    newFieldValue = input(f"Select a particular value for your choosen field: {fieldName} ")
    print(f"The new particular  value enterd is {newFieldValue}")
    # add single quotes arround the new field value
    # name  = Anna,  now name = " ' " + Anna + " ' "  = 'Anna'
    newFieldValue = "'" + newFieldValue + "'"
    print(f"The new field value enterd is {newFieldValue}")
    # Update the tblFilms table
    "UPDATE tblFilms SET(Title,Year Released,Rating,Duration,Genre) = newFieldValue(Dance/MJ/Pop) WHERE SongID = 1/2/3... "
    cursor.execute(
        f"SELECT * FROM tblFilms WHERE {fieldName} = {newFieldValue}"
    )

    conn.commit()
    time.sleep(3)
    # call/invoke the readSongs from readData
    readFilms()

if __name__ == "__main__":
    printfilmID()
