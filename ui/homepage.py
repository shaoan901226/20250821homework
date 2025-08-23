import tkinter as tk

class HomePage:
    def __init__(self, master):
        self.master = master
        self.master.title("首頁")
        self.master.state("zoomed")

        # grid 配置
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        # 文字置中
        tk.Label(self.master, text="歡迎來到首頁！", font=("Arial", 24)).grid(row=0, column=0, sticky="nsew")

        # 登出按鈕
        tk.Button(self.master, text="登出", font=("Arial", 14),
                  command=self.logout).grid(row=1, column=0, pady=20)

    def logout(self):
        self.master.destroy()