##functions example.

 
#Let's return to the music example from assignment one. Pick 3 of the attributes you listed. For our example 
#we're going to say "Genre", "Artist" and "Year". Create a new Python file and create 3 functions with the same name
#as those attributes. So in this example we'd have one function named "genre" another named "artist" and another called "year".

#When someone calls any of those functions, that function should return the corresponding value for that attribute. 
#For example, if we call the "Artist" function our function would return "Dave Brubeck". Yours should return whatever 
#values make sense for your music choice.


#Extra Credit:

#One of the data types we haven't covered yet is called "booleans". When a variable is set to True or False,
#that's a boolean. For extra credit, see if you can figure out how to use booleans, and add an extra function
#that returns a boolean value instead of a String or Number. Hint: make sure to capitalize the first letter
#in the words True or False when you use them. We'll cover booleans more in the lecture on "if" statements coming up next in the course.


#code snippet

def nameOfArtist():
    albumArtist = "Hillsong Live"
    return albumArtist

def songName():
    nameofSong = "Glorious Ruin"
    return nameofSong

def lengthofSong():
    durationInSeconds = 530
    return durationInSeconds

print(lengthofSong())
print(nameOfArtist())
print(songName())

# creating a boolean check with an existing function to just print 'True' or 'False' 

artistName = nameOfArtist()

confirmName = input("name of the artist:  ")
if confirmName == artistName :
  print("True")
else:
    print("False")

# create a new function to return either true or false after user inputs the name of the artist

#create a global variable 

AlbumArtist = "Hillsong Live"

def checkArtistName(value):
    # perform the checks here

    if AlbumArtist == value :
        return True
    else:
        return False

# user input here 

enterValue = input("what do you think is the name of the Artist ? :    ")
answer = checkArtistName(enterValue)

# system response

print(answer)