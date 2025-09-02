# HomePage.py
import tkinter as tk
from tkinter import messagebox

class HomePage:
    def __init__(self, master, account_repo, current_user):
        self.master = master
        self.account_repo = account_repo
        self.current_user = current_user

        self.master.title("首頁")
        self.master.state("zoomed")

        # 主框架
        frame = tk.Frame(master)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # 歡迎文字
        tk.Label(frame, text=f"歡迎 {self.current_user.username}！", font=("Arial", 24)).pack(pady=20)
        
        # 個人資料
        tk.Label(frame, text=f"性別: {self.current_user.gender}", font=("Arial", 14), width=25, anchor="w").pack(pady=5)
        tk.Label(frame, text=f"生日: {self.current_user.birthday}", font=("Arial", 14), width=25, anchor="w").pack(pady=5)
        tk.Label(frame, text=f"電子郵件: {self.current_user.email}", font=("Arial", 14), width=25, anchor="w").pack(pady=5)

        # 刪除帳號
        tk.Button(frame, text="刪除帳號", font=("Arial", 14), width=20, command=self.delete_account).pack(pady=20)
        # 登出
        tk.Button(frame, text="登出", font=("Arial", 14), width=20, command=self.logout).pack(pady=10)

    # 刪除帳號
    def delete_account(self):
        confirm = messagebox.askyesno("確認", f"確定要刪除帳號「{self.current_user.username}」嗎？")
        if confirm:
            success, msg = self.account_repo.delete_account(self.current_user.username)
            if success:
                messagebox.showinfo("成功", msg)
                self.logout()
            else:
                messagebox.showerror("錯誤", msg)

    # 登出
    def logout(self):
        self.master.destroy()
