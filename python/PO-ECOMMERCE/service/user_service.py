from dao.user_dao import UserDAO


class UserService:

    def __init__(self):
        self.user_dao = UserDAO()

    def register(self, name, email, password):
        self.user_dao.create_table()

        self.user_dao.register_user(name, email, password)

    def login(self, email, password):
        return self.user_dao.login_user(email, password)