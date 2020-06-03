

def implement(arr):
    #loop from 1 to end of array
    for i in range(1, len(arr)):
        temp = arr[i]


        j = i

        while j > 0 and temp < arr[j-1]:
            #copy element to left to this postiotino
            arr[j] = arr[j-1]

            j-= i

        arr[j] = temp

    return arr


    #sorting books!

class Book:
    def __init__(self, author, title, genre):
        self.author = author
        self.title = title
        self.genre = genre

    
    def __str__(self):
        return f'{self.title} by {self.author} in {self.genre}' 

books = [Book("mel", "moby dick", "whales"), Book("n","n", "n"), Book("s","s", "s"), Book("jk","jk", "jk"), Book("ty","ty", "ty")]

def insertion(books):
    for i in range(1, len(books)):
        temp = books[i]

        j = i
        
        # While were not at fron of list
        while j > 0 and temp.genre < books[j-1].genre:
            books[j] = books[j-1]
            j -= 1

        books[j] = temp

    return books

print(insertion(books))