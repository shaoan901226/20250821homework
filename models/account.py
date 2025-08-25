class AccountModel:
    def __init__(self):
        # 帳號資料格式：{username: password}
        self.accounts = {"user01": "24682468"}

    def add_account(self, username, password):
        if not username:
            return "使用者名稱不得為空白"
        if username in self.accounts:
            return "帳號已存在"
        self.accounts[username] = password
        return "成功創建帳號"

    def verify_account(self, username, password):
        if username in self.accounts and self.accounts[username] == password:
            return True
        return False

    def get_all_accounts(self):
        return list(self.accounts.keys())