import mysql.connector
import hashlib
from models.Account import Account
from Repository.DatabaseConfig import DatabaseConfig

class AccountRepo:
    def __init__(self, config: DatabaseConfig):
        try:
            self.conn = mysql.connector.connect(
                host=config.host,
                user=config.user,
                password=config.password,
                database=config.database
            )
            self.create_table()
        except Exception as e:
            print("資料庫連接失敗:", e)
            raise

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS account (
                    idAccount INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    gender VARCHAR(10),
                    birthday DATE,
                    email VARCHAR(255)
                )
            """)
            self.conn.commit()
        except Exception as e:
            print("建立表格失敗:", e)
            raise


    def hash_password(self, password: str) -> str:
        try:
            return hashlib.sha256(password.encode("utf-8")).hexdigest()
        except Exception as e:
            print("密碼哈希失敗:", e)
            raise

    def create_account(self, account: Account):
        try:
            if not account.username:
                return False, "使用者名稱不得為空白"
            
            if self.get_account(account.username):
                return False, "帳號已存在"

            hashed_pw = self.hash_password(account.password)
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO account (username, password, gender, birthday, email) VALUES (%s, %s, %s, %s, %s)",
                (account.username, hashed_pw, account.gender, account.birthday, account.email)
            )
            self.conn.commit()
            return True, "成功創建帳號"
        except Exception as e:
            print("創建帳號失敗:", e)
            return False, f"系統錯誤: {e}"


    def validate_login(self, username: str, password: str):
        try:
            acc = self.get_account(username)
            if not acc:
                return False, "帳號不存在"

            input_hashed = self.hash_password(password)
            if acc.password != input_hashed:
                return False, "密碼錯誤"

            return True, acc
        except Exception as e:
            print("驗證登入失敗:", e)
            return False, f"登入驗證失敗: {e}"

    def delete_account(self, username: str):
        try:
            if not self.get_account(username):
                return False, "帳號不存在"

            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM account WHERE username = %s", (username,))
            self.conn.commit()
            return True, "帳號已刪除"
        except Exception as e:
            print("刪除帳號失敗:", e)
            return False, f"系統錯誤: {e}"

    def get_account(self, username: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT username, password, gender, birthday, email FROM account WHERE username = %s",
                (username,)
            )
            row = cursor.fetchone()
            if row:
                return Account(*row)
            return None
        except Exception as e:
            print("查詢帳號失敗:", e)
            return None
