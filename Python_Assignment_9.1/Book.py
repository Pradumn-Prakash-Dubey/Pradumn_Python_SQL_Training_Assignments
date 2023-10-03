class Book:
    def __init__(self, id, title, author, price, rating):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

def find_book_by_id(books, id):
    for book in books:
        if book.id == id:
            return book
    return None


def find_books_by_author(books, author):
    books_by_author = []
    for book in books:
        if book.author == author:
            books_by_author.append(book)
    print("Books by author",author,"is :",end=" ")
    for item in books_by_author:
           print(item.title,sep=" ",end=" ")
    


def find_books_in_rating_range(books, min_rating, max_rating):
    books_in_rating_range = []
    for book in books:
        if book.rating >= min_rating and book.rating <= max_rating:
            books_in_rating_range.append(book)
    print("Books in Rating range",min_rating,":",max_rating,"is :",end=" ")
    for item in books_in_rating_range:
           print(item.title,sep=" ",end=" ")
           
    


def find_books_in_price_range(books, min_price, max_price):
    books_in_price_range = []
    for book in books:
        if book.price >= min_price and book.price <= max_price:
            books_in_price_range.append(book)
    print("Books in Price range Rs",min_price,"to","Rs",max_price,"is :",end=" ")
    for item in books_in_price_range:
           print(item.title,sep=" ",end=" ")
           

if __name__=="__main__":
    books = [
    Book(1, "P1", "Pradumn", 12.99, 4.5),
    Book(2, "M1", "Madhav", 29.99, 5.0),
    Book(3, "A1", "Akshit", 10.99, 4.7),
    Book(4, "H1", "Harshit", 11.99, 4.9),
    Book(5, "R1", "Raja", 13.99, 4.6),
]
book = find_book_by_id(books, 2)
print("Book with ID",book.id,"is",book.title)

find_books_by_author(books, "Pradumn")
print()

find_books_in_rating_range(books, 4.5, 5.0)
print()

find_books_in_price_range(books, 10.00, 15.00)
print()
