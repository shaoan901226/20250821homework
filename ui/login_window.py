import tkinter as tk
from tkinter import messagebox
from ui.homepage import HomePage

class LoginWindow:
    def __init__(self, master, account_model):
        self.master = master
        self.master.title("登入系統")
        self.master.state("zoomed")
        self.account_model = account_model

        self.frame = tk.Frame(master)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.frame, text="帳號:").grid(row=0, column=0, pady=5)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.frame, text="密碼:").grid(row=1, column=0, pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)

        tk.Button(self.frame, text="登入", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.frame, text="創建新帳號", command=self.open_create_account).grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, msg = self.account_model.validate_login(username, password)
        if success:
            self.show_success()
        else:
            messagebox.showerror("錯誤", msg)

    def open_create_account(self):
        create_win = tk.Toplevel(self.master)
        create_win.title("創建帳號")
        window_width, window_height = 350, 200
        x = (self.master.winfo_screenwidth() // 2) - (window_width // 2)
        y = (self.master.winfo_screenheight() // 2) - (window_height // 2)
        create_win.geometry(f"{window_width}x{window_height}+{x}+{y}")

        frame = tk.Frame(create_win)
        frame.pack(expand=True)

        tk.Label(frame, text="帳號:", font=("Arial", 12)).grid(row=0, column=0, pady=10, padx=10, sticky="e")
        username_entry = tk.Entry(frame, font=("Arial", 12), justify="left")
        username_entry.grid(row=0, column=1, pady=10, padx=10)

        tk.Label(frame, text="密碼:", font=("Arial", 12)).grid(row=1, column=0, pady=10, padx=10, sticky="e")
        password_entry = tk.Entry(frame, font=("Arial", 12), show="*", justify="left")
        password_entry.grid(row=1, column=1, pady=10, padx=10)

        def create_account_action():
            username = username_entry.get().strip()
            password = password_entry.get()
            success, msg = self.account_model.create_account(username, password)
            if success:
                messagebox.showinfo("成功", msg)
                create_win.destroy()
            else:
                messagebox.showerror("錯誤", msg)

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
        HomePage(homepage)