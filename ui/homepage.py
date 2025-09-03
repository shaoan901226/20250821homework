# HomePage.py
import tkinter as tk
from tkinter import messagebox

class HomePage:
    def __init__(self, master, account_repo, current_user):
        try:
            self.master = master
            self.account_repo = account_repo
            self.current_user = current_user
            self.master.title("首頁")
            self.master.state("zoomed")

            frame = tk.Frame(master)
            frame.place(relx=0.5, rely=0.5, anchor="center")

            tk.Label(frame, text=f"歡迎 {self.current_user.username}！", font=("Arial", 24)).pack(pady=20)
            tk.Label(frame, text=f"性別: {self.current_user.gender}", font=("Arial", 14), width=25, anchor="w").pack(pady=5)
            tk.Label(frame, text=f"生日: {self.current_user.birthday}", font=("Arial", 14), width=25, anchor="w").pack(pady=5)
            tk.Label(frame, text=f"電子郵件: {self.current_user.email}", font=("Arial", 14), width=25, anchor="w").pack(pady=5)

            tk.Button(frame, text="刪除帳號", font=("Arial", 14), width=20, command=self.delete_account).pack(pady=20)
            tk.Button(frame, text="登出", font=("Arial", 14), width=20, command=self.logout).pack(pady=10)
        except Exception as e:
            print("HomePage初始化失敗:", e)
            messagebox.showerror("錯誤", f"首頁初始化失敗: {e}")

    # 刪除帳號
    def delete_account(self):
        try:
            confirm = messagebox.askyesno("確認", f"確定要刪除帳號「{self.current_user.username}」嗎？")
            if confirm:
                success, msg = self.account_repo.delete_account(self.current_user.username)
                if success:
                    messagebox.showinfo("成功", msg)
                    self.logout()
                else:
                    messagebox.showerror("錯誤", msg)
        except Exception as e:
            print("刪除帳號失敗:", e)
            messagebox.showerror("錯誤", f"刪除帳號時發生錯誤: {e}")

    # 登出
    def logout(self):
        try:
            self.master.destroy()
        except Exception as e:
            print("登出失敗:", e)
            self.master.destroy()