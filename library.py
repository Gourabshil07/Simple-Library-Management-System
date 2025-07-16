class Mylibrary:
    def __init__(self,no_books,collection_books):
        self._no_books = no_books
        self._collection_books = collection_books

    
    # show books and amoutn of books

    def show_book_data(self):
        print(f"\nThe total number of books is: {self._no_books}\n")
        print("The Collection of books are:",", ".join(self._collection_books))
        
    

    @property
    def no_books(self):
        return self._no_books
    
    @property
    def collection_books(self):
        return self._collection_books
    
    @collection_books.setter
    def collection_books(self, new_books):
        self._collection_books = new_books
        self._no_books = len(self._collection_books)

    
    
    def search_book(self,book_name):
        for book in self._collection_books:
            if book.lower() == book_name.lower():
                print(f"✅ {book_name} book is available")
                return 
        print(f"{book_name} book is not available")


   
    def add_book(self, new_books):
        # for book in new_books:
            if new_books not in self._collection_books:
                self._collection_books.append(new_books)
                print(f" ✅ Book: {new_books} added Succesfully")
            else:
                print(f" ❎ Can't add {new_books} it's already exists")
            self._no_books= len(self._collection_books)


    def remove_book(self, book_name):
        if book_name in self._collection_books:
            self._collection_books.remove(book_name)
            self._no_books = len(self._collection_books)
            print(f"\n✅ {book_name} is removed successfully")
            return
        print("🔴 Book is not found")

lib = Mylibrary(0,[])

lib.collection_books = ["math", "English", "Biology","Chemistry","Computer Network","DBMS", "Numerical Method"]



while True:

    print("\n\n 📚📚 WELLCOME TO MY LIBRARY MANGAGEMENT SYSTEM\n\n")

    print("1. Search for a book:\n")
    print("2. Add a new book:\n")
    print("3. Remove a book:\n")
    print("4. Show all the books:\n ")
    print("5. Exit to the library\n")

    try:
        choice = int(input("Enter your choice(1-5): "))
        
    
        if choice == 1:
            search_book = input("Search books: ")
            lib.search_book(search_book)
            
        elif choice == 2:
            insert_book = input("Enter which book you want to add: ")
            lib.add_book(insert_book)
        elif choice == 3:
            remove_book = input("Enter which book you want to remove: ")
            lib.remove_book(remove_book)
        elif choice == 4:
            lib.show_book_data()

        elif choice == 5:
            print("Thanks for using the Library, have a good day \n")
            break
        else:
            print(" ❌ Invalid! input")

    except ValueError:
        print("❌ Invalid! please Enter number between (1-5)")
