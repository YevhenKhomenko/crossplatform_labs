class Users:
    def __init__(self):

        # mock instead of DB or text file
        self.users = []

    def add_user(self, name):
        self.users.append(name)

    def get_users(self):
        return self.users

    def delete_last_user(self):
        if self.users:
            self.users.pop()
            return True
        return False

