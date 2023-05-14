from sqlConnect import *
from readDatabase import readFilms
import time

# create a subroutine to add songs to the songs table
def addFilms():
    # create an emplty list
    films = []

    title = input("Enter film Title: ")
    yearReleased = input("Enter film Year Realeased: ")
    rating = input("Enter film Rating: ")
    duration = input("Enter film Duration: ")
    genre = input("Enter film Genre: ")

    # append data entered by user to song list
    "films.FilmId is set to auto increment and would be added in automatically"

    films.append(title) # append title
    films.append(yearReleased) # append artist
    films.append(rating)  # append genre
    films.append(duration) # append duration
    films.append(genre) #append genre

    #insert data from songs list into the song table
    cursor.execute("INSERT INTO tblFilms VALUES(NULL, ?,?,?,?,?)", films)
    conn.commit() # save changes permannetly to songs table

    print (f"Title{title} added to film table") # returns the title of the song added
    time.sleep(3)
    # retrieve the entire record of the song added to the database
    # cursor.execute("SELECT * FROM songs") # select all songs
    # row = cursor.fetchall() #fetch all records that was selected above
    # # iterate through all the fetched records
    # for record in row:
    #     print(record)
    readFilms()

if __name__ == "__main__":
    addFilms()