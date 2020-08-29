class library:
    def __init__(self, book_lst, lib_name):
        self.lend = {}
        self.other = {}
        self.book_lst = book_lst
        self.lib_name = lib_name
        for book in self.book_lst: #adding book from list using for loop
            self.lend[book] = None #making value to None

    def display(self):
        print("Displaying book's \n")
        for k,v in self.lend.items():
            print(k)
        print("---------------\n")


    def lend_book(self, book_name):
        # book_name = input("enter book you want to lend")
        if book_name in self.lend.keys():
            print(f"{book_name} :book is available for lend \n")
            user_name = input("enter your name for lending book \n")
            self.lend[book_name] = user_name
            print(f"{book_name} has been lended by {user_name} \n")
        else:
            print("entered book name does not exists into out dictinary \n")


    def add_book(self, add_book_name):
        # add_book_name = input("enter the book name to be added")
        if add_book_name in self.lend.keys():
            print(f"{add_book_name} already present in dictinray \n")
        else:
            self.lend[add_book_name] = None
            print(f"{add_book_name} added into our dictnonary \n")


    def return_book(self, book_name, user_name):
        if book_name in self.lend.keys() and user_name == self.lend.get(book_name):
            self.lend[book_name] = None
            print(f"{book_name} book has been return \n")

if __name__ == '__main__':
    l = library(["english", "urdu", "arabic", "marathi", "german"], "onlinelib")
    print(f"welcome to {l.lib_name} management")

    flag = True
    while flag:
        user_input = int(input(
            "1 .display\n "
            "2 .lend_book\n "
            "3 .add_book\n "
            "4. return_book\n "
            "5. Exit \n "
            "Enter no. to select menu\n"))

        if user_input == 1:
            l.display()
            # break
        elif user_input == 2:
            book_name = input("enter book name you wanna LEND \n").lower()
            l.lend_book(book_name)
            # break
        elif user_input == 3:
            book_name = str(input("enter book name that you wanna ADD \n"))
            l.add_book(book_name)
            # break
        elif user_input == 4:
            book_name = input("enter book name that you wanna RETURN \n").lower()
            user_name = input(f"enter user name to RETURN {book_name}\n").lower()
            l.return_book(book_name,user_name)
            # break

        elif user_input == 5:
            flag = False
        else:
            print("!!!! please enter correct menu number !!!! \n")