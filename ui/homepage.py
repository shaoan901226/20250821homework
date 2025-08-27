import tkinter as tk
from tkinter import messagebox

class HomePage:
    def __init__(self, master, account_model, current_user):
        self.master = master
        self.account_model = account_model
        self.current_user = current_user
        self.master.title("首頁")
        self.master.state("zoomed")

        # 內容置中
        frame = tk.Frame(self.master)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text=f"歡迎 {self.current_user}！", font=("Arial", 24)).pack(pady=40)
        tk.Button(frame, text="刪除帳號", font=("Arial", 14), command=self.delete_account).pack(pady=20)
        tk.Button(frame, text="登出", font=("Arial", 14), command=self.logout).pack(pady=20)

    def delete_account(self):
        confirm = messagebox.askyesno("確認", f"確定要刪除帳號「{self.current_user}」嗎？")
        if confirm:
            success, msg = self.account_model.delete_account(self.current_user)
            if success:
                messagebox.showinfo("成功", msg)
                self.logout()
            else:
                messagebox.showerror("錯誤", msg)

    def logout(self):
        self.master.destroy()