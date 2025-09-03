from Repository.DatabaseConfig import DatabaseConfig
from Repository.AccountRepo import AccountRepo
from ui.LoginWindow import LoginWindow
import tkinter as tk

def main():
    try:
        config = DatabaseConfig(user="root", password="Ray880203==", database="userdb")
        repo = AccountRepo(config)
        
        root = tk.Tk()
        app = LoginWindow(root, repo)
        root.mainloop()
        
    except Exception as e:
        print("程式啟動失敗:", e)
        input("程式啟動失敗，按 Enter 鍵退出...")

if __name__ == "__main__":
    main()