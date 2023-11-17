
print("Welcome to the music app: Myusik! \n")


genres = ["rock", "hip hop", "pop", "country", "jazz"]


def AddAlbum(allRatings):
    validInputs = ["rock", "hip hop", "pop", "country", "jazz", "list"]

    userGenre = input(
        "To start, enter a genre you'd like to enter, or enter 'list' for a list of the genres you may enter: ")
    userGenre = userGenre.lower()

    while userGenre not in validInputs:
        userGenre = input(
            "Invalid input, try again or enter 'list' to see a list of valid inputs: ")
        userGenre = userGenre.lower()

    if (userGenre == "list"):
        print("The list of genres you can enter is ")
        for item in validInputs:
            if (item != "list"):
                print(item + " | ")
                return
    userAlbum = input("Now enter the name of the album: ")
    userRating = input("Now enter your rating for the album: ")
    for i in range(0, len(allRatings) - 1):
        if (userGenre == allRatings[i].genre):
            (allRatings[i].ratings).append(userRating)
            (allRatings[i].albums).append(userAlbum)

    PrintRatingsInGenre(allRatings, "rock")


def PrintRatingsInGenre(allRatings, genre):
    for i in range(len(allRatings)):
        if (genre == allRatings[i].genre):
            print("The ratings in " + genre + " are as follows: \n")
            for r in range(len(allRatings[i].ratings)):
                print(str(allRatings[i].albums[r]) + ": " +
                      str(allRatings[i].ratings[r]) + "\n")


class GenreRatings:
    def __init__(self, genre, ratings, albums):
        self.genre = genre
        self.ratings = ratings
        self.albums = albums


rockRatings = GenreRatings(genre="rock", ratings=[], albums=[])
hiphopRatings = GenreRatings(genre="hiphop", ratings=[], albums=[])
popRatings = GenreRatings(genre="pop", ratings=[], albums=[])
countryRatings = GenreRatings(genre="country", ratings=[], albums=[])
jazzRatings = GenreRatings(genre="jazz", ratings=[], albums=[])
allRatings = [rockRatings, hiphopRatings,
              popRatings, countryRatings, jazzRatings]

for i in range(1, 5):
    AddAlbum(allRatings)
