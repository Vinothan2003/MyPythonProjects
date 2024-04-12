from datetime import datetime


def greetings(value) -> None:
    print('-' * 10, value, '-' * 10)


def message(value) -> None:
    print('-' * 2, value, '-' * 2)


def title_msg(value) -> None:
    print('-' * 5, value, '-' * 5)


def date_time():
    date_and_time = datetime.now()
    print(date_and_time.strftime("TIME - %I:%M %p\nDATE - %Y-%B-%d"))


class InvalidOperationError(Exception):
    pass
