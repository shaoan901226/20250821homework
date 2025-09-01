import mysql.connector
import hashlib

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AccountRepo:
    def __init__(self, host="localhost", user="root", password="", database="userdb"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS account (
                idAccount INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """)
        self.conn.commit()

    def hash_password(self, password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def create_account(self, username, password):
        if not username:
            return False, "使用者名稱不得為空白"
        if self.get_account(username):
            return False, "帳號已存在"

        hashed_pw = self.hash_password(password)
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO account (username, password) VALUES (%s, %s)",
                (username, hashed_pw)
            )
            self.conn.commit()
            return True, "成功創建帳號"
        except Exception as e:
            return False, f"資料庫錯誤: {e}"

    def validate_login(self, username, password):
        acc = self.get_account(username)  # 改成呼叫自己
        if not acc:
            return False, "帳號不存在"

        hashed_pw = self.hash_password(password)
        if acc.password != hashed_pw:
            return False, "密碼錯誤"

        return True, "登入成功"

    def delete_account(self, username):
        if not self.get_account(username):
            return False, "帳號不存在"
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM account WHERE username = %s", (username,))
        self.conn.commit()
        return True, "帳號已刪除"

    def get_account(self, username):
        cursor = self.conn.cursor()
        cursor.execute("SELECT username, password FROM account WHERE username = %s", (username,))
        row = cursor.fetchone()
        if row:
            return Account(*row)  # 建立 Account 物件
        return None