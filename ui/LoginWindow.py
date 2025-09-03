import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from models.Account import Account
from ui.HomePage import HomePage

class LoginWindow:
    def __init__(self, master, account_repo):
        try:
            self.master = master
            self.account_repo = account_repo
            self.master.title("登入系統")
            self.master.state("zoomed")

            frame = tk.Frame(master)
            frame.place(relx=0.5, rely=0.5, anchor="center")

            tk.Label(frame, text="帳號:").grid(row=0, column=0, pady=5, sticky="e")
            self.username_entry = tk.Entry(frame)
            self.username_entry.grid(row=0, column=1, pady=5)

            tk.Label(frame, text="密碼:").grid(row=1, column=0, pady=5, sticky="e")
            self.password_entry = tk.Entry(frame, show="*")
            self.password_entry.grid(row=1, column=1, pady=5)

            tk.Button(frame, text="登入", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
            tk.Button(frame, text="創建新帳號", command=self.open_create_account).grid(row=3, column=0, columnspan=2, pady=10)
        except Exception as e:
            print("LoginWindow初始化失敗:", e)
            messagebox.showerror("錯誤", f"程式初始化失敗: {e}")

    def login(self):
        try:
            username = self.username_entry.get()
            password = self.password_entry.get()
            
            success, result = self.account_repo.validate_login(username, password)
            if success:
                self.show_success(result)
            else:
                messagebox.showerror("錯誤", result)
        except Exception as e:
            print("登入失敗:", e)
            messagebox.showerror("錯誤", f"登入過程中發生錯誤: {e}")

    def open_create_account(self):
        try:
            if hasattr(self, "create_win") and self.create_win.winfo_exists():
               self.create_win.lift()
               return

            self.create_win = tk.Toplevel(self.master)
            self.create_win.title("創建帳號")
            window_width, window_height = 400, 350
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            x = (screen_width // 2) - (window_width // 2)
            y = (screen_height // 2) - (window_height // 2)
            self.create_win.geometry(f"{window_width}x{window_height}+{x}+{y}")
            self.create_win.resizable(False, False)

            frame = tk.Frame(self.create_win)
            frame.place(relx=0.5, rely=0.5, anchor="center")

            tk.Label(frame, text="帳號:", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="e")
            username_entry = tk.Entry(frame, font=("Arial", 12))
            username_entry.grid(row=0, column=1, pady=5)

            tk.Label(frame, text="密碼:", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="e")
            password_entry = tk.Entry(frame, font=("Arial", 12), show="*")
            password_entry.grid(row=1, column=1, pady=5)

            tk.Label(frame, text="性別:", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky="e")
            gender_combo = ttk.Combobox(frame, values=["男", "女", "其他"], state="readonly", font=("Arial", 12))
            gender_combo.grid(row=2, column=1, pady=5)
            gender_combo.current(0)

            tk.Label(frame, text="生日:", font=("Arial", 12)).grid(row=3, column=0, pady=5, sticky="e")
            birthday_entry = DateEntry(frame, font=("Arial", 12), date_pattern='yyyy-mm-dd')
            birthday_entry.grid(row=3, column=1, pady=5)

            tk.Label(frame, text="電子郵件:", font=("Arial", 12)).grid(row=4, column=0, pady=5, sticky="e")
            email_entry = tk.Entry(frame, font=("Arial", 12))
            email_entry.grid(row=4, column=1, pady=5)

            def create_account_action():
                try:
                    username = username_entry.get().strip()
                    password = password_entry.get()
                    gender = gender_combo.get()
                    birthday = birthday_entry.get_date()
                    email = email_entry.get().strip()

                    if not email or "@" not in email or "." not in email.split("@")[-1]:
                       messagebox.showerror("錯誤", "請輸入有效的電子郵件")
                       email_entry.focus_set()
                       return

                    birthday_str = birthday.strftime('%Y-%m-%d')
                    account = Account(username, password, gender, birthday_str, email)
                    success, msg = self.account_repo.create_account(account)
                
                    if success:
                        messagebox.showinfo("成功", msg)
                        self.create_win.destroy()
                        created_account = self.account_repo.get_account(username)
                        if created_account:
                            self.show_success(created_account)
                        else:
                            messagebox.showerror("錯誤", "帳戶建立成功但無法獲取資訊")
                            self.create_win.destroy()
                    else:
                        messagebox.showerror("錯誤", msg)
                        username_entry.focus_set()
                except Exception as e:
                    print("創建帳號失敗:", e)
                    messagebox.showerror("錯誤", f"創建帳戶時發生異常: {e}")

            # 按鈕創建應該在 try 區塊內，與其他 UI 元素同一層級
            tk.Button(frame, text="確定", font=("Arial", 12), width=10, command=create_account_action).grid(row=5, column=0, columnspan=2, pady=20)
            
        except Exception as e:
            print("開啟創建帳號視窗失敗:", e)
            messagebox.showerror("錯誤", f"無法開啟創建帳號視窗: {e}")
        
        
    def show_success(self, account):
        try:
            self.master.withdraw()
            homepage_win = tk.Toplevel(self.master)
            HomePage(homepage_win, self.account_repo, account)
            homepage_win.protocol("WM_DELETE_WINDOW", lambda: self.on_homepage_close(homepage_win))
        except Exception as e:
            print("顯示成功畫面失敗:", e)
            messagebox.showerror("錯誤", f"無法顯示首頁: {e}")


