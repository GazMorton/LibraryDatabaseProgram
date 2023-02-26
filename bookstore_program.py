import sqlite3

RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

# Adding books to the database
def add_book(id, Title, Author, Qty):
    sqlite_insert = '''INSERT INTO books (id,title,author,qty) VALUES (?,?,?,?)'''
    data_tuple = (id,Title,Author,Qty)
    cursor.execute(sqlite_insert,data_tuple)
    db.commit()

# Update book quantity
def update_book(id):
    id
    qty = input('please enter the new quantity:\n')
    cursor.execute('''UPDATE books SET qty = ? WHERE id = ? ''',(qty,id))
    db.commit()

# Delete book from database
def delete_book(id):
    cursor.execute('''DELETE FROM books WHERE id = ? ''', (id,))
    db.commit()

# Search books in the database using one of three criteria depending on whether user knows the id, title or author
def search_book_id(id):
    cursor.execute('''SELECT id, title, author, qty FROM books WHERE id = ?''', (id,))
    for row in cursor: 
        print('\n{0} | {1} | {2} | {3}'.format(row[0], row[1], row[2], row[3]))


def search_book_title(title):
    cursor.execute('''SELECT id, title, author, qty FROM books WHERE title = ?''', (title,))
    for row in cursor: 
        print('\n{0} | {1} | {2} | {3}'.format(row[0], row[1], row[2], row[3]))


def search_book_author(author):
    cursor.execute('''SELECT id, title, author, qty FROM books WHERE author = ?''', (author,))
    for row in cursor: 
        print('\n{0} | {1} | {2} | {3}'.format(row[0], row[1], row[2], row[3]))

# Added a view all books function
def view_all_books():
    cursor.execute('''select * from books''')
    for row in cursor: 
        print('{0} | {1} | {2} | {3}'.format(row[0], row[1], row[2], row[3]))


# ============= END OF FUNCTIONS ==========================================  
# Create a database connection
db = sqlite3.connect('ebookstore')

cursor = db.cursor()

# Created books table with desired fields
cursor.execute('''CREATE TABLE books (id INT PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')

db.commit()

id1 = 3001
title1 = 'A Tale of Two Cities'
author1 = 'Charles Dickens'
qty1 = 30

id2 = 3002
title2 = 'Harry Potter and the Philosopher\'s Stone'
author2 = 'J.K. Rowling'
qty2 = 40

id3 = 3003
title3 = 'The Lion, the Witch and the Wardrobe'
author3 = 'C.S. Lewis'
qty3 = 25

id4 = 3004
title4 = 'The Lord of the Rings'
author4 = 'J.R.R Tolkien'
qty4 = 37

id5 = 3005
title5 = 'Alice in Wonderland'
author5 = 'Lewis Carroll'
qty5 = 12

books = [(id1,title1,author1,qty1), (id2,title2,author2,qty2), (id3,title3,author3,qty3), (id4,title4,author4,qty4), (id5,title5,author5,qty5)]

# Inserting multiple rows at once using executemany
cursor.executemany(''' INSERT INTO books (id, title, author, qty) VALUES(?,?,?,?)''',books)

db.commit()

#========================== DATABASE MENU SECTION ===============================
while True:
    print(f"""           
        {RED}╔══════════════════════╗{END}
        {BOLD}   BOOKSTORE DATABASE 
        {RED}╚══════════════════════╝{END}
    """)
    print('')
    option = int(input("""please select an option from the below:\n
🔸 1 - Enter book
🔸 2 - Update book
🔸 3 - Delete book
🔸 4 - Search books
🔸 5 - View all books
🔸 6 - Exit\n"""))

# Calling functions and asking for arguements to be input by user
    if option == 1:
        add_book(input('id:'), input('Title:'), input('Author:'), input('Quantity:'))

    elif option == 2:
        update_book(int(input('Please enter the id of the book you\'d like to update:\n')))

    elif option == 3:
        delete_book(input('Please enter the id of the book you\'d like to delete:\n'))

# added another conditional so users can narrow down their search based on desired search criteria
    elif option == 4:
        
        while True:
            search_criteria = input('''\nSearch by:
🔸 1 - id
🔸 2 - title
🔸 3 - author\n''')
            if search_criteria == '1':
                search_book_id(input('Please enter an id to search for a book:\n'))
                break
            elif search_criteria == '2':
                search_book_title(input('Please enter a title to search for a book using Title case:\n'))
                break
            elif search_criteria == '3':
                search_book_author(input('Please enter an author to search for books:\n'))
                break
            else:
                print('Please choose a valid option')
                continue
    elif option == 5:
        view_all_books()
    
    elif option == 6:
        print(f'\n═════════════════ 👋 Goodbye!! 👋 ══════════════════\n')
        exit()

    else:
        print('Oops, you have not selected a valid option, please try again')