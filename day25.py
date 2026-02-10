#person
class Person:
    def _init_(self, id, name):
        self.id = id
        self.name = name

#books
class Book:
    def _init_(self,id, name, author):
        self.id = id
        self.name = name
        self.author = author

#users
class Users(Person):
    def _init_(self, id, name):
        super()._init_(id, name)

class Admin(Person):
    def _init_(self, id:int, name):
        super()._init_(id, name)

    def Add_book(self, book_obj:Book, quantity:int):
        if book_obj.id not in books:
            books[book_obj.id] = [book_obj.name,book_obj.author, quantity]
            return f'{book_obj.name} has been added successfully'
        
        return f'Book already exists'

    #add new user
    def add_user(self, user_obj:Users):
        if user_obj.id not in users:
            users[user_obj.id] = {'name':user_obj.name, 'books_id':[]}
            return f'{user_obj.name} has been added successfully'
        
        return f'User already exists'



    def delete_book(self, bookid):
        if bookid in books:
            books.pop(bookid)
            return f'Book is {bookid} removed successfully'
        return f'Book id {bookid} does not exist'

    def barrow_book(self, userid, *bookids):
        if userid in users:
            avl_books = []
            unavl_books = []   
            for bookid in bookids:
                if bookid in books:
                    if books[bookid][2] > 0:
                        avl_books.append({bookid:books[bookid][0]})
                        books[bookid][2] -= 1
                        users[userid]['books_id'].append(bookid)
                    else:
                        unavl_books.append({bookid:books[bookid][0]})
                else:
                    unavl_books.append({bookid:books[bookid][0]})
            return f'Available books are: {avl_books} and unavailable books are: {unavl_books}'
        return "user not found"
                    

    def return_book(self, userid, *bookids):
        if userid in users:   
            for bookid in bookids:
                if bookid in books and users[userid]['books_id']:
                    books[bookid][2] += 1 # increment of quantity
                    users[userid]['books_id'].remove(bookid) #-->remove book from user
            
            return f'Books returned successfully'
        return "user not found"
    def all_books(self):
        return books
    def all_users(self):
        return len(users)
    

#main
if _name_ == "_main_":
    print("Welcome to Library Management System")

    admin = Admin(101, "premsai")

    while True:
        print("select your operation: \n1. Add book \n2. Register user \n3.Barrow book \n4.Return book \n5.view all book \n6.Total users \n7.delete book\ n8.Exit from library")
        choice = int(input("Enter your choice"))
        if choice == 1:
            bookid = int(input("Enter book id"))
            name = input("Enter book name")
            author = input("Enter author name")
            quantity = int(input("Enter quantity"))
            # creating book obj
            book_obj = Book(bookid, name, author)
            #add book to library
            print(admin.Add_book(book_obj, quantity))
        elif choice == 2:
            user_id = int(input("Enter user id"))
            user_name = input("Enter user name")
            user_obj = Users(user_id, user_name) #--> creating user object
            print(admin.add_user(user_obj))# --> adding user
        elif choice == 3:
            print("your selected option is barrow")
            user_id = int(input("enter user id"))
            book_ids = list(map(int, input("enter book ids:").split(",")))
            print(admin.barrow_book(user_id, *book_ids))
        elif choice == 4:
            print("your selected option is Return books")
            user_id = int(input("enter user id"))
            book_ids = list(map(int, input("enter book ids:").split(",")))
            print(admin.return_book(user_id, *book_ids))
        elif choice == 5:
            print("your selected option is 5 view all books")
            all_books = admin.all_books()
            print(f"Book Id | Book Name |Author Name | Quantity")
            for bookid, details in all_books.items():
                print(f'Book id: {bookid}, Book name: {details[0]}, Author: {details[1]}, Quantity: {details[2]}')
        elif choice == 6:
            print("your selected option is 6 total users")
            print(admin.all_users())
        elif choice == 7:
            print("your selected option is 7 delete book")
            bookid = int(input("Enter book id"))
            print(admin.delete_book(bookid=bookid))
        elif choice == 8:
            print("Thank you selected option is 8 Exit")
            print("Bye,your are successfully exit from library management system")
            break
        else:
            print("Invalid choice, please select a valid option(1-8)")