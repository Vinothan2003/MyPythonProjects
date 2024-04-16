import json


class GymMembers:
    @staticmethod
    def new_member_data(name, age, gender, contact_no, aadhar_no, package, amount):
        with open("gym/members_data/member_details.json", 'r') as read_file:  # reding the json file
            existing_data = json.load(read_file)  # deserialization

        member_details = {'name': name, 'age': age, 'gender': gender, 'contact_no': contact_no, 'aadhar_no': aadhar_no,
                          'package_selection': package, 'amount': amount}
        existing_data.append(member_details)  # appending value
        print(existing_data)

        with open("gym/members_data/member_details.json", 'w') as write_file:  # writing the file
            json.dump(existing_data, write_file)  # serialization


if __name__ == '__main__':
    gym = GymMembers()
    gym.new_member_data("Akash", 20, 'male', 9789619430,
                        111122223333, 'M', 20000)
