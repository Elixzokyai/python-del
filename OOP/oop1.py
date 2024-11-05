# Write code to manage a lib. collection. The lib should be able to add books , remove books and list all books

# functional programming
# initial lib collection (sequences : lists, tuples, sets, dictionaries )
lib_collection = []  # intialize the collection as an empty list

def add(theCurrentCollection,book):
    # using .append in functional programming modifies the original list and does not return a new list
    # .append + mutable , create a new list and updates the version of the list on subsequent calls
    currentCollection = theCurrentCollection + [book]
    print(currentCollection)
    return currentCollection


def remove(theCurrentCollection, book):
    return theCurrentCollection.remove(book)

def list_books(theCurrentCollection):
    # list out the books on iteration
    for book in theCurrentCollection:
        print(book)

# usage
library_collection = add(lib_collection,"Book1")
print(library_collection)
# list_books(library_collection)
# library_collection = add(library_collection,"Book2")
# list_books(library_collection)
# library_collection = add(library_collection,"Book3")
# list_books(library_collection)
# library_collection = remove(library_collection,"Book3")
# list_books(library_collection)

"""
Pros 
1. Function being stateless do not depend on external states , making reuse easy. Each call operates independently 

Cons 
1. Managing the states become cumbersome because we need to pass the collection explicity each time and return the updated 
collection

2. Functional programming : emphasis is on immutablity 

"""

"""
OOP address 
1. Pros 
Encapsulation allows management of state within the object, Methods belong to the class , so we do not need to pass the 
collection explicitly / each time. Extension and management is modularized in code 

2. Cons 
More complex than functional programming for simple tasks.  Requires more setup with class definations and instances
"""

class Library:
    def __init__(self):
        self.collection = []

    def addBook(self,book):
        self.collection.append(book)

    def removeBook(self,book):
        if book in self.collection:
            self.collection.remove(book)

    def listBooks(self):
         for book in self.collection:
             print(book)


library1 = Library()
library1.addBook("The great gatsby")
library1.addBook("The great gatsby 2")
library1.addBook("The great gatsby 3")
library1.listBooks()
library1.removeBook("The great gatsby 2")
library1.listBooks()