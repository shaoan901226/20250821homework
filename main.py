import tkinter as tk
from models.account import Account
from ui.login_window import LoginWindow

if __name__ == "__main__":
    accounts = [
        Account("user01", "123456"),
        Account("admin", "admin123")
    ]

    root = tk.Tk()
    app = LoginWindow(root, accounts)
    root.mainloop()