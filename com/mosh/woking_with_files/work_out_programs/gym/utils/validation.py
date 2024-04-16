class InvalidOperationError(Exception):
    pass


class Verification:

    @staticmethod
    def details_validation(name: str, age: int, gender: str, contact_no: int, aadhar_no: int):
        if not name.isalpha():
            error_msg("Provide correct name")
            return False
        if not age > 13:
            error_msg("Age must be greater than 13\nOtherwise your not allowed to gym")
            return False
        if not gender.isalpha() and gender not in ['male', 'female']:
            error_msg("Provide correct gender")
            return False
        if len(str(contact_no)) != 10:
            error_msg("Invalid Contact Number")
            return False
        if len(str(aadhar_no)) != 12:
            error_msg("Invalid Aadhar Number")
            return False
        return True

    @staticmethod
    def package_validation(package, value):
        if package == 'M':
            if not 1 <= value <= 9:
                error_msg("Select Proper Monthly Package")
                return False
        elif package == 'Y':
            if not 1 <= value <= 3:
                error_msg("Select Proper Yearly Package")
                return False
        return True

    @staticmethod
    def payment_validation(required_amount, user_amount):
        if user_amount != required_amount:
            error_msg("Invalid Amount")
        return user_amount


def greetings(value):
    print("-" * 10, value, "-" * 10)


def error_msg(value):
    print("-" * 3, value, "-" * 3)
