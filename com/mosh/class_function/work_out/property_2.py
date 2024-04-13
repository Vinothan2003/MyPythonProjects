class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def user_name(self):
        return self.name

    @user_name.setter
    def user_name(self, value):
        print(f"{self.name} is changed to {value}")
        self.name = value

    @user_name.deleter
    def user_name(self):
        del self.user_name
        
    @property
    def user_password(self):
        return self.password

    @user_password.setter
    def user_password(self, value):
        print(f"Password is changed")

    @user_password.deleter
    def user_password(self):
        del self.user_password


user = User(name="Vinothan", password="hello123")
print(user.user_name, user.password)

user.user_name = "Hello"
print(user.user_name, user.password)

user.user_password = "123423"

del user.user_name
del user.user_password
