from com.mosh.library_management.utils.validation import greetings, message


class MemberManagement:
    def __init__(self):
        self.members = [("vinothan", "vinothan@ncv.org")]

    def member_ship_validation(self, member_info):
        flag = False
        for member_list in self.members:
            if member_info[0] == member_list[0] and member_info[1] == member_list[1]:
                flag = True
                message("Access Granted")
                return flag
        if not flag:
            message("Access Denied")
            return flag

    def add_member(self, member_name: str, member_email: str) -> None:
        member_info = (member_name, member_email)
        self.members.append(member_info)
        greetings("Member Added")
        print(f"Member Name : {member_name}\nMember Email : {member_email}")

    def display_members(self):
        greetings("Member List")
        for member_list in self.members:
            print(member_list)

    def remove_member(self, member_name: str, member_email_id: str) -> None:
        flag = False
        for member_list in self.members:
            if member_name == member_list[0] and member_email_id == member_list[1]:
                flag = True
                self.members.remove(member_list)
                greetings("Member Removed")
                print(f"Member Name : {member_name}\nMember Email-id - {member_email_id}")
        if not flag:
            print("---Member Not Found---")


if __name__ == '__main__':
    member = MemberManagement()
    member.add_member("vinothan", "@gmail.com")
    member.remove_member("vinothan", "@gmail.com")
