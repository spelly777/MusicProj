# music rating app yurrr day one yurrrrrrrr
# Next steps to add more functionality to viewing the ratings and add favorite song functionality + average rating for genres
# basically add more UI functionality - allow the user to do what they want
# also, potentially have function definitions in a different file to allow for better formatted code

from musicRatingMethods import AddAlbum, PrintGenreRating, PrintAllRatings
import sys
sys.path.append(".")

allRatings = []


class Rating:
    def __init__(self, genre, albums, ratings):
        self.genre = genre
        self.ratings = ratings
        self.albums = albums


allRatings = []
print("\n\n Hello, and welcome to the music rating app Myusik! \n\n")
print("There are a few options available currently, however the app will be constantly expanding. ")
userSelection = '0'
while (userSelection == '0'):
    print("1. Enter a new album to rate\n2. View current ratings of a genre\n3. View all ratings entered\n4. Exit program\n\n ")
    userSelection = input("Enter the number of your selection here:")

    if (userSelection == '1'):
        AddAlbum(allRatings)
        userSelection = '0'
    elif (userSelection == '2'):
        PrintGenreRating(allRatings)
        userSelection = '0'
    elif (userSelection == '3'):
        PrintAllRatings(allRatings)
        userSelection = '0'
    elif (userSelection == '4'):
        print("\n\nThank you for using Myusik, have an awesome day :)")
        exit()
    else:
        userSelection = '0'
        print("Invalid input, try again \n")
