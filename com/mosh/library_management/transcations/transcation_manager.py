from com.mosh.library_management.utils.validation import greetings, date_time
from datetime import datetime


class History:
    def __init__(self):
        self.transaction_history = []
        self.transaction_outsider_history = []

    @staticmethod 
    def date_history():
        date = datetime.now()
        return date.strftime("%Y-%b-%d")

    def display_transactions(self):
        greetings("Transaction History")
        for display in self.transaction_history:
            print(display)

    def take_book(self, book_name, member_name):
        today_date = History.date_history()
        history = (book_name, member_name, today_date)
        self.transaction_history.append(history)
        greetings("Transaction History --> Book Taken")
        print(f"Book Name : {book_name}\nMember Name : {member_name}")
        date_time()

    def return_book(self, book_name, member_name):
        flag = False
        for history in self.transaction_history:
            if book_name == history[0] and member_name == history[1]:
                flag = True
                self.transaction_history.remove(history)

                greetings("Transaction History --> Book Returned")
                print(f"Book Name : {book_name}\nMember Name : {member_name}")
                date_time()
        if not flag:
            print("---Transaction Not Made---")

    def outsider(self, book_name, os_mail, os_aadhar):
        today_date = History.date_history()
        history = (book_name, os_mail, os_aadhar, today_date)
        self.transaction_history.append(history)
        greetings("Transaction History --> Book Taken")
        print(f"Book Name : {book_name}\nOutsider Mail : {os_mail}\nOutsider Aadhar : {os_aadhar}")
        date_time()


if __name__ == '__main__':
    his = History()
    his.return_book("vinotasfdsa", "asdfsafsadfs")
    his.display_transactions()
    his.take_book("vinotasfdsa", "asdfsafsadfs")
    his.display_transactions()
