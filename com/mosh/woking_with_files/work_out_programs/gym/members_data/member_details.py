import json
from com.mosh.woking_with_files.work_out_programs.gym.data_base.gym_details import GymDataBase
from com.mosh.woking_with_files.work_out_programs.gym.utils.validation import msg
from datetime import *


class GymMembers:

    @staticmethod
    def new_member_data(name, age, gender, contact_no, aadhar_no, package, amount, valid_date):
        gym_database = GymDataBase()

        member_details = [{'name': name, 'age': age, 'gender': gender, 'contact_no': contact_no,
                           'aadhar_no': aadhar_no,
                           'package_selection': package, 'amount': amount, 'Validity_date': valid_date}]

        with open("gym/members_data/member_details.json", 'w') as write_file:  # reding the json file
            json.dump(member_details, write_file)  # serialization

        gym_database.members_data()
        gym_database.display_members()

        with open("gym/data_base/all_members_details.json", 'r') as read_file:
            existing_data = json.load(read_file)
            for member in existing_data:
                if member['name'] == name:
                    print(f"Your Gym ID : {member['id']}")

    @staticmethod
    def existing_member(gym_id):
        gym_database = GymDataBase()
        with open("gym/data_base/all_members_details.json", 'r') as read_file:
            existing_data = json.load(read_file)
            for member in existing_data:
                if member['id'] == gym_id:
                    msg("Access Granted")
                    return True, member['Validity_date']
            else:
                msg("Access Denied")
                return False

    def update_package(self, gym_id, amount, validity, package):
        gym_database = GymDataBase()
        with open("gym/data_base/all_members_details.json", 'r') as read_file:
            existing_data = json.load(read_file)

        for member in existing_data:
            if member['id'] == gym_id:
                member['amount'] = amount
                member['Validity_date'] = validity
                member['package_selection'] = package

        with open("gym/data_base/all_members_details.json", 'w') as write_file:
            json.dump(existing_data, write_file)

        gym_database.update_validity(gym_id=gym_id, package=package, amount=amount, validity=validity)

        msg("Gym Package Recharge Successfully")


if __name__ == '__main__':
    gym = GymMembers()
    gym.new_member_data(None, "Akash", "20", 'male', 9789619430, 111122223333, 'M', 20000, 2025 - 9 - 6)
