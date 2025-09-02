from Repository.DatabaseConfig import DatabaseConfig
from Repository.AccountRepo import AccountRepo
from ui.LoginWindow import LoginWindow
import tkinter as tk

config = DatabaseConfig(user="root", password="Ray880203==", database="userdb")
repo = AccountRepo(config)

root = tk.Tk()
app = LoginWindow(root, repo)
root.mainloop()