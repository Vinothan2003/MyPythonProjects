from books.book_manager import BookManagement
from members.member_manager import MemberManagement
from transcations.transcation_manager import History
from utils.validation import InvalidOperationError, greetings, message, title_msg


def member_ship():
    user_name = input("> Name : ").lower().strip()
    user_mail = input("> Mail-ID : ").lower().strip()
    if user_mail.endswith("@ncv.org"):
        return user_name, user_mail
    else:
        return "-Invali Mail-ID, eg-(xxxxxxx@ncv.com)-"


def outsider():
    outsider_name = input("> Your Name : ").lower().strip()
    outsider_mail_id = input("> Your Mail-ID : ").strip()
    outsider_Aadhar_number = input("> Your Aadhar Number : ")
    if outsider_Aadhar_number.isdigit() and '@' in outsider_mail_id:
        print("Pay the Book Amount in the 'Counter'")
        return outsider_name, outsider_mail_id, outsider_Aadhar_number
    else:
        print("Provide Valid Aadhar Number and Email-ID")
        return "--Try Again--"


def main():
    greetings("NCV Library")
    user_response: str = 'yes'
    while True:

        try:
            if user_response == 'yes':
                user_validation = input("Do you have Membership Yes | No :  ").lower().strip()
                if user_validation == 'yes':
                    member_validation = member_ship()
                    print(member_validation)
                    if member_manage.member_ship_validation(member_validation):
                        user_action = input("> Take | Return (Book) : ").lower().strip()
                        if user_action == "take":
                            title_msg("This Books are Available")
                            book_manage.display_books()
                            book_taken_name = input("> Borrow Book Name : ").lower().strip()
                            book_taken_author = input("> Borrow Book Author Name : ").lower().strip()
                            if book_manage.remove(book_name=book_taken_name, book_author=book_taken_author):
                                transaction_history.take_book(book_name=book_taken_name,
                                                              member_name=member_validation[0])
                        elif user_action == "return":
                            book_return_name = input("> Return Book Name : ")
                            book_return_author = input("> Return Book Author Name : ")
                            book_manage.add(book_name=book_return_name, book_author=book_return_author)
                            transaction_history.return_book(book_name=book_return_name,
                                                            member_name=member_validation[0])
                        else:
                            message("Invalid Action")

                elif user_validation == 'no':
                    print("Note : You have to Pay Amount(Safety purpose) for the Book")
                    outsider_info = outsider()
                    print(outsider_info)
                    title_msg("This Books are Available")
                    book_manage.display_books()
                    os_book_borrow_name = input("> Borrow Book Name : ")
                    os_book_borrow_author = input("> Borrow Book Author Name : ")
                    if book_manage.remove(book_name=os_book_borrow_name, book_author=os_book_borrow_author):
                        transaction_history.outsider(book_name=os_book_borrow_name, os_mail=outsider_info[1],
                                                     os_aadhar=outsider_info[2])
                    print("Return the book in counter while returning")

                else:
                    raise InvalidOperationError("Invalid Input")

            elif user_response == "no":
                greetings("Thank You, Welcome again")
                quit()
            else:
                message("Invalid Operation")

            user_response = input("Continue Yes | No : ").lower().strip()
        except InvalidOperationError as error:
            message(error)


if __name__ == '__main__':
    book_manage = BookManagement()
    member_manage = MemberManagement()
    transaction_history = History()
    main()
