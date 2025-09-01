import tkinter as tk
from tkinter import messagebox
from Repository import AccountRepo
from ui.HomePage import HomePage

class LoginWindow:
    def __init__(self, master, account_repo):
        self.master = master
        self.master.title("登入系統")
        self.master.state("zoomed")  # 最大化
        self.account_repo = account_repo

        self.frame = tk.Frame(master)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.frame, text="帳號:").grid(row=0, column=0, pady=5)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.frame, text="密碼:").grid(row=1, column=0, pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)

        # 登入按鈕
        tk.Button(self.frame, text="登入", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
        # 創建新帳號按鈕
        tk.Button(self.frame, text="創建新帳號", command=self.open_create_account).grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, msg = self.account_repo.validate_login(username, password)
        if success:
            self.show_success()
        else:
            messagebox.showerror("錯誤", msg)

    def open_create_account(self):
        # 檢查視窗是否已經存在
        if hasattr(self, "create_win") and self.create_win.winfo_exists():
            self.create_win.lift()  # 把已存在的視窗帶到最前面
            return

        # 建立創建帳號視窗
        self.create_win = tk.Toplevel(self.master)
        self.create_win.title("創建帳號")
        self.create_win.state("zoomed")

        # 中間置中設定
        window_width, window_height = 350, 200
        x = (self.master.winfo_screenwidth() // 2) - (window_width // 2)
        y = (self.master.winfo_screenheight() // 2) - (window_height // 2)
        self.create_win.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 內容 Frame
        frame = tk.Frame(self.create_win)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="帳號:", font=("Arial", 12)).grid(row=0, column=0, pady=10, padx=10, sticky="e")
        username_entry = tk.Entry(frame, font=("Arial", 12))
        username_entry.grid(row=0, column=1, pady=10, padx=10)

        tk.Label(frame, text="密碼:", font=("Arial", 12)).grid(row=1, column=0, pady=10, padx=10, sticky="e")
        password_entry = tk.Entry(frame, font=("Arial", 12), show="*")
        password_entry.grid(row=1, column=1, pady=10, padx=10)

        # 確定按鈕動作
        def create_account_action():
            username = username_entry.get().strip()
            password = password_entry.get()
            success, msg = self.account_repo.create_account(username, password)
            if success:
                messagebox.showinfo("成功", msg)
                self.create_win.destroy()  # 成功才關閉視窗
                del self.create_win       # 移除屬性
            else:
                messagebox.showerror("錯誤", msg)
                username_entry.focus_set()  # 保持視窗開啟，聚焦帳號輸入框

        tk.Button(frame, text="確定", font=("Arial", 12), width=10, command=create_account_action)\
            .grid(row=2, column=0, columnspan=2, pady=20, padx=10)

    def show_success(self):
        success_window = tk.Toplevel(self.master)
        success_window.title("登入成功")
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
        HomePage(homepage, self.account_repo, self.username_entry.get())