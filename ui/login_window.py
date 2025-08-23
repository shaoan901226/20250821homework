import tkinter as tk
from tkinter import messagebox
from ui.homepage import HomePage

class LoginWindow:
    def __init__(self, master, accounts):
        self.master = master
        self.accounts = accounts
        self.master.title("登入系統")
        self.master.state("zoomed")

        # grid 配置
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

        # 中間框架
        frame = tk.Frame(master)
        frame.grid(row=1, column=1)

        tk.Label(frame, text="帳號:", font=("Arial", 14)).grid(row=0, column=0, pady=10, padx=10)
        self.username_entry = tk.Entry(frame, font=("Arial", 14))
        self.username_entry.grid(row=0, column=1, pady=10, padx=10)

        tk.Label(frame, text="密碼:", font=("Arial", 14)).grid(row=1, column=0, pady=10, padx=10)
        self.password_entry = tk.Entry(frame, show="*", font=("Arial", 14))
        self.password_entry.grid(row=1, column=1, pady=10, padx=10)

        tk.Button(frame, text="登入", font=("Arial", 14), command=self.login).grid(row=2, column=0, columnspan=2, pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        account = next((acc for acc in self.accounts if acc.username == username), None)

        if account:
            if account.verify_password(password):
                self.show_success()
            else:
                messagebox.showerror("錯誤", "帳號或密碼錯誤")
        else:
            messagebox.showerror("錯誤", "帳號不存在")

    def show_success(self):
        success_window = tk.Toplevel(self.master)
        success_window.title("登入成功")

        # 對話框置中
        window_width, window_height = 300, 150
        x = (self.master.winfo_screenwidth() // 2) - (window_width // 2)
        y = (self.master.winfo_screenheight() // 2) - (window_height // 2)
        success_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tk.Label(success_window, text="登入成功！", font=("Arial", 16)).pack(pady=20)
        tk.Button(success_window, text="確定", font=("Arial", 14),
                  command=lambda: [success_window.destroy(), self.open_homepage()]).pack(pady=10)

    def open_homepage(self):
        self.master.withdraw()
        homepage = tk.Toplevel(self.master)
        HomePage(homepage)