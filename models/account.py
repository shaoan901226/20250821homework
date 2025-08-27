import json
import os

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return {"username": self.username, "password": self.password}

    @staticmethod
    def from_dict(data):
        return Account(data["username"], data["password"])

class AccountModel:
    def __init__(self, filepath="accounts.json"):
        self.filepath = filepath
        self.accounts = self.load_accounts()

    def load_accounts(self):
        print(f"嘗試讀取帳號從 {self.filepath}")
        if not os.path.exists(self.filepath):
            print("找不到帳號檔案")
            return {}
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            print("讀取到帳號：", data)
            return {u: Account.from_dict(acc) for u, acc in data.items()}

    def save_accounts(self):
        print(f"儲存帳號到 {self.filepath}")
        with open(self.filepath, "w", encoding="utf-8") as f:
            data = {u: acc.to_dict() for u, acc in self.accounts.items()}
            print("要儲存的帳號：", data)
            json.dump(data, f, ensure_ascii=False, indent=2)

    def create_account(self, username, password):
        if not username:
            return False, "使用者名稱不得為空白"
        if username in self.accounts:
            return False, "帳號已存在"
        self.accounts[username] = Account(username, password)
        self.save_accounts()
        return True, "成功創建帳號"

    def validate_login(self, username, password):
        if username not in self.accounts:
            return False, "帳號不存在"
        if self.accounts[username].password != password:
            return False, "密碼錯誤"
        return True, "登入成功"
    
    def delete_account(self, username):
        if username not in self.accounts:
            return False, "帳號不存在"
        del self.accounts[username]
        self.save_accounts()
        return True, "帳號已刪除"