def AddAlbum(allRatings):
    validInputs = ["rock", "hip hop", "pop", "country", "jazz",
                   "list"]  # declare inputs available for user to enter

    userGenre = input(
        "To start, enter a genre you'd like to enter, or enter 'list' for a list of the genres you may enter: ")
    userGenre = userGenre.lower()

    while (userGenre not in validInputs) or (userGenre == 'list'):
        if (userGenre == "list"):  # list inputs to enter if 'list' entered
            print("The list of genres you can enter is ")
            for item in validInputs:
                if (item != "list"):
                    print(item + " | ", end="")
            print()
            userGenre = input("\n Enter a genre from the list: ")
        else:
            userGenre = input(
                "Invalid input, try again or enter 'list' to see a list of valid inputs: ")  # validate input
        userGenre = userGenre.lower()

    # get name of album to add
    userAlbum = input("Now enter the name of the album: ")
    # get rating of album to add
    userScore = input("Now enter your rating for the album: ")
    newAlbumRating = Rating(userGenre, userAlbum, userScore)
    allRatings.append(newAlbumRating)


def PrintGenreRating(allRatings):
    validInputs = ["rock", "hip hop", "pop", "country", "jazz",
                   "list"]
    userGenre = input(
        "Enter a genre to print the ratings of, or enter 'list' to see a list of entries: ")
    userGenre = userGenre.lower()
    while (userGenre not in validInputs) or (userGenre == 'list'):
        if (userGenre == "list"):  # list inputs to enter if 'list' entered
            print("The list of genres you can enter is ")
            for item in validInputs:
                if (item != "list"):
                    print(item + " | ", end="")
            print()
            userGenre = input("\n Enter a genre from the list: ")
        else:
            userGenre = input(
                "Invalid input, try again or enter 'list' to see a list of valid inputs: ")  # validate input
        userGenre = userGenre.lower()
    print("The ratings in " + userGenre + " are as follows: \n")
    for i in range(len(allRatings)):
        if (userGenre == allRatings[i].genre):
            print(str(allRatings[i].album) + ": " +
                  str(allRatings[i].rating) + "\n")


def PrintAllRatings(allRatings):
    for item in allRatings:
        print(str(item.album) + ": " + str(item.rating) + "\n")
        print("\n")


class Rating:
    def __init__(self, genre, album, rating):
        self.genre = genre
        self.rating = rating
        self.album = album
