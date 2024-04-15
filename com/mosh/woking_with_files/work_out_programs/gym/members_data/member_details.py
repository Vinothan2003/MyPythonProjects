import json
from pathlib import Path


class GymMembers:
    def new_member_data(self, name, age, gender, contact_no, aadhar_no, payment_selection, amount):
        member_details = {'name': name, 'age': age, 'gender': gender, 'contact_no': contact_no, 'aadhar_no': aadhar_no,
                          'payment_selection': payment_selection, 'amount': amount}

        data = json.dumps(member_details)
        Path("member_details.json").write_text(data)


if __name__ == '__main__':
    gym = GymMembers()
    gym.new_member_data("vinothan", 20, 'male', 9789619430,
                        111122223333, 'M', 20000)
