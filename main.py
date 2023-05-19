from getpass import getpass
from user import User

def user_menu(self):
        while True:
            print("\n1. Display User Information")
            print("2. Edit Personal Information")
            print("3. Change Password")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                print(self)
            elif choice == "2":
                new_username = input("Enter new username: ")
                if new_username != self.username and new_username in User.users_dict:
                    print("Username is already taken. Please choose another username.")
                else:
                    new_number_phone = input("Enter new phone number (optional): ")
                    self.username = new_username
                    self.number_phone = new_number_phone
                    print("Personal information updated successfully.")
                    print(self)
            elif choice == "3":
                current_password = getpass("Enter current password: ")
                new_password = getpass("Enter new password: ")
                confirm_password = getpass("Confirm new password: ")

                if User.verify_password(current_password, self.password) and new_password == confirm_password \
                        and User.validate_password(new_password):
                    self.password = User.encrypt_password(new_password)
                    print("Password changed successfully.")
                else:
                    print("Password change unsuccessful.")
            elif choice == "4":
                print("Logout successful.")
                break
            else:
                print("Invalid choice. Please try again.")


def register_user():
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    number_phone = input("Enter phone number (optional): ")

    user = User(username, password, number_phone)
    print("User registered successfully.")
    print(user)


def login_user():
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    if username in User.users_dict:
        user = User.users_dict[username]
        if User.verify_password(password, user.password):
            print("Login successful.")
            user.user_menu()
        else:
            print("Invalid username or password.")
    else:
        print("Invalid username or password.")


def main_menu():
    while True:
        print("\n0. Exit")
        print("1. Register User")
        print("2. Login")
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Program terminated.")
            break
        elif choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()