class InvalidOperationError(Exception):
    pass


class Verification:
    @staticmethod
    def details_validation(name: str, age: int, gender: str, contact_no: int, aadhar_no: int):
        if not name.isalpha():
            print("Provide correct name")
            return False
        if not age > 13:
            print("Age must be greater than 13\nOtherwise your allowed to gym")
            return False
        if not gender.isalpha():
            print("Provide correct gender")
            return False
        if len(str(contact_no)) != 10:
            print("Invalid Contact Number")
            return False
        if len(str(aadhar_no)) != 12:
            print("Invalid Aadhar Number")
            return False
        return True


def greetings(value):
    print("-" * 10, value, "-" * 10)
