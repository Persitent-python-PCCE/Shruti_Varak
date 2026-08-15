from service.user_service import UserService


class UserController:

    def __init__(self):
        self.user_service = UserService()

    def register(self):
        print("\n--- Register ---")

        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        self.user_service.register(name, email, password)

    def login(self):
        print("\n--- Login ---")

        email = input("Enter email: ")
        password = input("Enter password: ")

        user = self.user_service.login(email, password)

        if user:
            print("Login successful!")
            print("Welcome", user[1])

            return user
        else:
                print("Invalid email or password!")
                return None