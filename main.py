import tkinter as tk
from models.account import AccountModel
from ui.login_window import LoginWindow

if __name__ == "__main__":
    model = AccountModel()
    root = tk.Tk()
    app = LoginWindow(root, model)
    root.mainloop()