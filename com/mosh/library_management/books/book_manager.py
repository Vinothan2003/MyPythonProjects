from com.mosh.library_management.utils.validation import greetings, date_time
from datetime import datetime


class BookManagement:

    def __init__(self):
        self.books = [('python programming', 'gudio van rossum', '2024-Apr-12'),
                      ('atomic habits', 'james clear', '2024-Apr-12'),
                      ("harry potter and the sorcerer's stone", 'j.k.rowling', '2024-Apr-12'),
                      ('harry potter and the chamber of secrete ', 'j.k.rowling', '2024-Apr-12')]

    @staticmethod
    def date_history():
        date = datetime.now()
        return date.strftime("%Y-%b-%d")

    def display_books(self):

        for books_info in self.books:
            print(books_info)

    def add(self, book_name, book_author):
        today_date = BookManagement.date_history()
        book_info = (book_name, book_author, today_date)
        self.books.append(book_info)
        greetings("Book Added")
        print(f"Book Name : {book_name}\nBook author :{book_author}")
        date_time()

    def remove(self, book_name, book_author):
        flag = False
        for book_info in self.books:
            if book_name in book_info[0] and book_author in book_info[1]:
                flag = True
                self.books.remove(book_info)
                return flag
        if not flag:
            print("---Book Unavailable---")
            return flag


if __name__ == '__main__':
    books = BookManagement()
    books.add("core java", "vinothan nc")
    greetings("Books")
    books.display_books()
