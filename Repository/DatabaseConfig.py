class DatabaseConfig:
    """資料庫設定"""
    def __init__(self, host="localhost", user="root", password="", database="userdb"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database