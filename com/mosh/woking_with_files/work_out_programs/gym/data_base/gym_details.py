import sqlite3
import json
from pathlib import Path


class GymDataBase:
    def members_data(self):
        json_file = Path("gym/members_data/member_details.json")
        with open(json_file, 'r') as file:
            json_data = json.load(file)

        with sqlite3.connect("gym/data_base/member.sqlite3") as update_file:
            update_command = "INSERT INTO Gym_Members (name,age,gender,contact_no,aadhar_no,package,amount,valid_date) Values (?, ?, ?, ?, ?, ?, ?, ?)"
            for details in json_data:
                update_file.execute(update_command, tuple(details.values()))
            update_file.commit()

    def display_members(self):
        with sqlite3.connect("gym/data_base/member.sqlite3") as read_file:
            read_command = "SELECT * FROM Gym_Members"
            cursor = read_file.execute(read_command)
            member_details = [{'id': row[0], 'name': row[1], 'age': row[2], 'gender': row[3], 'contact_no': row[4],
                               'aadhar_no': row[5],
                               'package_selection': row[6], 'amount': row[7], 'Validity_date': row[8]} for row in
                              cursor]

        with open("gym/data_base/all_members_details.json", 'w') as write_json:
            json.dump(member_details, write_json)

    def login_info(self, gym_id, log_date, log_time, log_session):
        with sqlite3.connect("gym/data_base/login_details.sqlite3") as file:
            command = "INSERT INTO Login_Details VALUES (?, ?, ?, ?)"
            file.execute(command, (gym_id, log_date, log_time, log_session))
            file.commit()

    def update_validity(self, gym_id, package, amount, validity):
        with sqlite3.connect("gym/data_base/member.sqlite3") as update_file:
            update_command = "UPDATE Gym_Members SET package = ?, amount = ?, valid_date = ?  where id = ?"
            update_file.execute(update_command, (package, amount, validity, gym_id))
            update_file.commit()


if __name__ == '__main__':
    gym_database = GymDataBase()
    gym_database.display_members()
