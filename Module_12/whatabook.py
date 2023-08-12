# Name: Autumn Gooding
# Date: August 7, 2023
# Class: CYBER410
# whatabook database final assignment

# Database contains the tables:
#   stores: hours, location
#   user: user_id, email, first_name, last_name
#   book: book_id, book_name, author, details
#   wishlist: wishlist_id, book_id, user_id

#import statements with MySQL
import sys
import mysql.connector
from mysql.connector import errorcode


def show_menu():
    print("\n  -- Main Menu --")
    print("\n Menu Options")
    
    print("    1. Books\n    2. Store Locations\n    3. My Account\n    4. Exit Program")


def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    
    books = _cursor.fetchall()
    
    print("\n  -- DISPLAYING BOOK INFO --")
    
    for book in books: 
        print("Book ID: {}\n Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2], book[3]))


def show_location(_cursor):
        _cursor.execute("SELECT store_id, locale FROM store")

        stores = _cursor.fetchall()

        print( "\n -- DISPLAYING STORE LOCATIONS -- \n")
        
        for store in stores:
            print("Store ID: {}\n Store Location: {}\n".format(store[0], store[1]))

def validate_user():
        users_id = input("\n Enter a USER ID or 4 to exit (Type number and press ENTER) ")

        # while users_choice is not one of the accepted inputs
        while users_id not in ['1', '2', '3', '4']:
            users_id = input("\n Your choice was not understood. Please try again: ")

        return users_id

def show_account_menu():
    
    print("\n -- USER Account Menu -- ")
    print("\n Menu Options")
     
    print("    1. Wishlist\n    2. Add Book to Wishlist\n    3. Exit to Main Menu\n")



def show_wishlist(_cursor, _user_id):
    # join book, user and wishlist tables to get all relevant information
    _cursor.execute("SELECT book.book_id, book.book_name, book.author, book.details \
                    FROM user \
                    INNER JOIN wishlist\
                        ON user.user_id = wishlist.user_id\
                    INNER JOIN book\
                        ON book.book_id = wishlist.book_id \
                    WHERE user.user_id = {};".format(_user_id))


    wishlists = _cursor.fetchall()
        
    print("\n -- DISPLAYING WISHLIST INFO -- \n")

    for wishlist in wishlists: 
        print("Book ID: {}\n Book Name: {}\n Author: {}\n Details: {}\n".format(wishlist[0], wishlist[1], wishlist[2], wishlist[3]))


def show_books_to_add(_cursor, _user_id):
    print("\n-- Books that can be added to wishlist --\n")

    query = "SELECT book_id, book_name, author, details \
             FROM book\
             WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id)
    
    _cursor.execute(query)

    new_books = _cursor.fetchall()

    for book in new_books: 
        print("Book ID: {}\n Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2], book[3]))

    new_book_ids = [str(book[0]) for book in new_books]
    
    return new_book_ids
    

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    # add book to users wishlist
    query = "INSERT INTO wishlist (user_id, book_id) VALUES ({}, {});".format(_user_id, _book_id)
    _cursor.execute(query)

    print("\n-- Displaying Updated Wishlist --\n")
    
    show_wishlist(_cursor, _user_id)
    



# Connecting to the WHATABOOK Database/ configuring database let user interact with program

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

try:
    # main application logic goes within this try block
    
    # Will use this to connect to the whatabook database
    db = mysql.connector.connect(**config)

    # create cursor instance for this connection
    cursor = db.cursor()
    
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

    # stay in main menu until user exits
    while True:

         # display menu to user
        show_menu()

        # get users menu choice
        users_choice = input("\n Choose an option from the menu (Type number and press Enter): ")
        
        # while users_choice is not one of the accepted inputs
        while users_choice not in ['1', '2', '3', '4']:
            users_choice = input("\n Your choice was not understood. Please try again: ")
        
        # do something depending on user's menu choice
        # 1. View books
        if users_choice == '1':

            # show the available books
            show_books(cursor)
    
        elif users_choice == '2':
            
            show_location(cursor)

        elif users_choice == '3':
            
            # make sure user is valid
            user_id = validate_user()

            # if user entered 4 to exit
            if user_id == '4':
                pass
               
            # otherwise user_id in ['1', '2', '3']
            else:

                while True:
                    # show user account menu and collect menu choice from user
                    show_account_menu()
                    
                    users_choice = input("\n Choose an option from the menu (Type number and press Enter): ")
            
                    # while users_choice is not one of the accepted inputs
                    while users_choice not in ['1', '2', '3']:
                        users_choice = input("\n Your choice was not understood. Please try again: ")

                    if users_choice == '1':
                        
                        show_wishlist(cursor, user_id)
                        

                    elif users_choice == '2':
                    
                        while True:

                            # display available books
                            new_book_ids = show_books_to_add(cursor, user_id)
                            new_book_ids += ['0']

                            # allow user to make choice
                            users_choice = input("\n Enter a book id to add to wishlist or enter 0 to go back: ")

                            while users_choice not in new_book_ids:
                                users_choice = input("\n Your choice was not understood. Please try again: ")

                            # go back to account menu
                            if users_choice == '0':
                                break

                            # a valid book id was entered, add it to wishlist
                            else:
                                book_id = users_choice
                                # prompt user to add a book
                                add_book_to_wishlist(cursor, user_id, book_id)

                    elif users_choice == '3':
                        # go back to main menu
                        break

        elif users_choice == '4':
            break
            



except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    #This will end the session

    db.close()
