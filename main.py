import tkinter as tk
from Repository.AccountRepo import AccountRepo
from ui.LoginWindow import LoginWindow

if __name__ == "__main__":
    model = AccountRepo(user="root", password="Ray880203==", database="userdb")
    root = tk.Tk()
    app = LoginWindow(root, model)
    root.mainloop()