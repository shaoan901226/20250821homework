import mysql.connector
import hashlib
from models.Account import Account
from Repository.DatabaseConfig import DatabaseConfig

class AccountRepo:
    def __init__(self, config: DatabaseConfig):
        # 建立資料庫連線
        self.conn = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )
        # 初始化資料表
        self.create_table()

    def create_table(self):
        """建立 account 表格（如果不存在）"""
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

    def hash_password(self, password: str) -> str:
        """使用 SHA-256 雜湊密碼"""
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def create_account(self, account: Account):
        """新增帳號"""
        if not account.username:
            return False, "使用者名稱不得為空白"
        if self.get_account(account.username):
            return False, "帳號已存在"

        hashed_pw = self.hash_password(account.password)
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO account (username, password, gender, birthday, email) VALUES (%s, %s, %s, %s, %s)",
                (account.username, hashed_pw, account.gender, account.birthday, account.email)
            )
            self.conn.commit()
            return True, "成功創建帳號"
        except Exception as e:
            return False, f"資料庫錯誤: {e}"

    def validate_login(self, username: str, password: str):
        """驗證登入帳號與密碼"""
        acc = self.get_account(username)
        if not acc:
            return False, "帳號不存在"

        if acc.password != self.hash_password(password):
            return False, "密碼錯誤"

        return True, acc

    def delete_account(self, username: str):
        """刪除帳號"""
        if not self.get_account(username):
            return False, "帳號不存在"

        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM account WHERE username = %s", (username,))
        self.conn.commit()
        return True, "帳號已刪除"

    def get_account(self, username: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT username, password, gender, birthday, email FROM account WHERE username = %s",(username,))
            row = cursor.fetchone()
            if row:
                return Account(*row)
            return None

        except Exception as e:
            print("發生未知錯誤:", e)
            return None
