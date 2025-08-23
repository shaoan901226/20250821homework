class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_password(self, password):
        return self.password == password