from sqlConnect import *



def readFilms():
    # Retrieve the inserted songs
    cursor.execute("SELECT * FROM tblFilms")  # select all songs
    row = cursor.fetchall()  # fetch all songs that was selected above
    # iterate through all the fetched records
    for record in row:
        print(record)


if __name__ == "__main__":
    readFilms()
