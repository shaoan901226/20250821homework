import tkinter as tk
import json
import os
from models.account import AccountModel
from ui.login_window import LoginWindow

if __name__ == "__main__":
    model = AccountModel(user="root", password="Ray880203==", database="userdb")
    root = tk.Tk()
    app = LoginWindow(root, model)
    root.mainloop()