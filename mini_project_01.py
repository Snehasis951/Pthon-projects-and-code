# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# GloabalLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

class Library:
    def __init__(self, list, name):
        self.books_List = list
        self.name = name
        self.lend_Dict = {}
    def display_Books(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.books_List:
            print(book)
    def lend_Book(self, user, book):
        if book not in self.lend_Dict.keys():
            self.lend_Dict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lend_Dict[book]}")
    def add_Book(self, book):
        self.books_List.append(book)
        print("Book has been added to the book list")
    def return_Book(self, book):
        self.lend_Dict.pop(book)
if __name__ == '__main__':
    Snehasis = Library(['Python', 'C++', 'Jango', 'HTML CSS JavaScript', 'Backend and Server'], "Gloabal_Library")
    while(True):
        print(f"Welcome to the {Snehasis.name} library. Enter your choice to continue")
        print("1) Display Books")
        print("2) Lend a Book")
        print("3) Add a Book")
        print("4) Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            Snehasis.display_Books()
        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            Snehasis.lend_Book(user, book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            Snehasis.add_Book(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            Snehasis.return_Book(book)
        else:
            print("Not a valid option")
        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
        if user_choice2 == "q":
                exit()

        elif user_choice2 == "c":
                continue



