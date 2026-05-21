# '''
# requests 库的使用
# '''
# import requests

# # 基本 GET 请求
# response = requests.get('https://api.github.com')
# # 带参数的 GET 请求
# params = {'key1': 'value1', 'key2': 'value2'}
# response = requests.get('https://httpbin.org/get', params=params)
# # 查看响应
# print(response.status_code)  # 状态码
# print()
# print(response.text)          # 响应内容（文本）
# print()
# print(response.url)           # 请求 URL
# print() 
# print(response.content)       # 响应内容（字节）
# print()
# print(response.json())        # 解析 JSON 响应
# print()
# print(response.headers)       # 响应头


import tkinter as tk
from tkinter import messagebox

# ====================== 银行账户类（核心业务逻辑）======================
class BankAccount:
    def __init__(self, account_id, name, password, balance=0):
        self.account_id = account_id          # 公开属性：账号
        self.name = name                      # 公开属性：姓名
        self.__password = password            # 私有属性：密码
        self.__balance = balance              # 私有属性：余额

    # 查询余额（返回余额或错误信息）
    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            return "密码错误"

    # 存款
    def deposit(self, password, amount):
        if password != self.__password:
            return "密码错误"
        if amount <= 0:
            return "存款金额必须大于0"
        self.__balance += amount
        return f"存款成功，当前余额：{self.__balance}"

    # 取款
    def withdraw(self, password, amount):
        if password != self.__password:
            return "密码错误"
        if amount <= 0:
            return "取款金额必须大于0"
        if self.__balance < amount:
            return "余额不足"
        self.__balance -= amount
        return f"取款成功，当前余额：{self.__balance}"

    # 修改密码
    def change_password(self, old_password, new_password):
        if old_password != self.__password:
            return "原密码错误"
        self.__password = new_password
        return "密码修改成功"

    # 获取账户基本信息（用于显示）
    def get_info(self):
        return f"账号：{self.account_id}，姓名：{self.name}"


# ====================== 可视化界面（基于 tkinter）======================
class BankSystemGUI:
    def __init__(self, master):
        self.master = master
        master.title("银行账户管理系统")
        master.geometry("500x500")
        master.resizable(False, False)

        # 存储所有账户：account_id -> BankAccount对象
        self.accounts = {}

        # ---------- 开户区域 ----------
        tk.Label(master, text="=== 开户 ===", font=("Arial", 12, "bold")).pack(pady=5)

        frame_open = tk.Frame(master)
        frame_open.pack(pady=5)

        tk.Label(frame_open, text="账号：").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.entry_open_id = tk.Entry(frame_open, width=15)
        self.entry_open_id.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_open, text="姓名：").grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.entry_open_name = tk.Entry(frame_open, width=15)
        self.entry_open_name.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_open, text="密码：").grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.entry_open_pwd = tk.Entry(frame_open, width=15, show="*")
        self.entry_open_pwd.grid(row=2, column=1, padx=5, pady=2)

        tk.Label(frame_open, text="确认密码：").grid(row=3, column=0, padx=5, pady=2, sticky="e")
        self.entry_open_pwd2 = tk.Entry(frame_open, width=15, show="*")
        self.entry_open_pwd2.grid(row=3, column=1, padx=5, pady=2)

        tk.Label(frame_open, text="初始余额：").grid(row=4, column=0, padx=5, pady=2, sticky="e")
        self.entry_open_balance = tk.Entry(frame_open, width=15)
        self.entry_open_balance.grid(row=4, column=1, padx=5, pady=2)
        self.entry_open_balance.insert(0, "0")

        btn_open = tk.Button(frame_open, text="开户", command=self.open_account, bg="lightgreen", width=10)
        btn_open.grid(row=5, column=0, columnspan=2, pady=8)

        # ---------- 分隔线 ----------
        tk.Label(master, text="=" * 40).pack(pady=5)

        # ---------- 账户操作区域 ----------
        tk.Label(master, text="=== 账户操作 ===", font=("Arial", 12, "bold")).pack(pady=5)

        frame_op = tk.Frame(master)
        frame_op.pack(pady=5)

        # 账号、密码输入
        tk.Label(frame_op, text="账号：").grid(row=0, column=0, padx=5, pady=4, sticky="e")
        self.entry_op_id = tk.Entry(frame_op, width=15)
        self.entry_op_id.grid(row=0, column=1, padx=5, pady=4)

        tk.Label(frame_op, text="密码：").grid(row=1, column=0, padx=5, pady=4, sticky="e")
        self.entry_op_pwd = tk.Entry(frame_op, width=15, show="*")
        self.entry_op_pwd.grid(row=1, column=1, padx=5, pady=4)

        # 金额输入（存款/取款用）
        tk.Label(frame_op, text="金额：").grid(row=2, column=0, padx=5, pady=4, sticky="e")
        self.entry_amount = tk.Entry(frame_op, width=15)
        self.entry_amount.grid(row=2, column=1, padx=5, pady=4)
        self.entry_amount.insert(0, "0")

        # 新密码输入（修改密码用）
        tk.Label(frame_op, text="新密码：").grid(row=3, column=0, padx=5, pady=4, sticky="e")
        self.entry_new_pwd = tk.Entry(frame_op, width=15, show="*")
        self.entry_new_pwd.grid(row=3, column=1, padx=5, pady=4)

        # 功能按钮区域
        frame_buttons = tk.Frame(master)
        frame_buttons.pack(pady=10)

        btn_query = tk.Button(frame_buttons, text="查询余额", command=self.query_balance, bg="#CCE5FF", width=10)
        btn_query.grid(row=0, column=0, padx=5)

        btn_deposit = tk.Button(frame_buttons, text="存款", command=self.deposit, bg="#CCE5FF", width=10)
        btn_deposit.grid(row=0, column=1, padx=5)

        btn_withdraw = tk.Button(frame_buttons, text="取款", command=self.withdraw, bg="#CCE5FF", width=10)
        btn_withdraw.grid(row=0, column=2, padx=5)

        btn_change_pwd = tk.Button(frame_buttons, text="修改密码", command=self.change_password, bg="#CCE5FF", width=10)
        btn_change_pwd.grid(row=0, column=3, padx=5)

        # ---------- 提示信息显示区域 ----------
        self.info_label = tk.Label(master, text="欢迎使用银行账户管理系统", fg="blue", wraplength=450, justify="left")
        self.info_label.pack(pady=15)

    # 显示消息（绿色成功 / 红色错误）
    def show_info(self, msg, is_error=False):
        color = "red" if is_error else "green"
        self.info_label.config(text=msg, fg=color)
        # 同时将消息记录到控制台（便于调试）
        print(msg)

    # 开户操作
    def open_account(self):
        acc_id = self.entry_open_id.get().strip()
        name = self.entry_open_name.get().strip()
        pwd = self.entry_open_pwd.get()
        pwd2 = self.entry_open_pwd2.get()
        balance_str = self.entry_open_balance.get().strip()

        # 输入校验
        if not acc_id or not name or not pwd:
            self.show_info("账号、姓名、密码不能为空！", is_error=True)
            return
        if pwd != pwd2:
            self.show_info("两次输入的密码不一致！", is_error=True)
            return
        try:
            balance = float(balance_str)
            if balance < 0:
                self.show_info("初始余额不能为负数！", is_error=True)
                return
        except ValueError:
            self.show_info("初始余额必须是数字！", is_error=True)
            return

        if acc_id in self.accounts:
            self.show_info(f"账号 {acc_id} 已存在，请使用其他账号！", is_error=True)
            return

        # 创建账户并存储
        new_account = BankAccount(acc_id, name, pwd, balance)
        self.accounts[acc_id] = new_account
        self.show_info(f"开户成功！{new_account.get_info()}，初始余额：{balance}")
        # 开户成功后清空开户表单的密码和确认密码（保留账号姓名方便连续开户？但清空关键字段）
        self.entry_open_pwd.delete(0, tk.END)
        self.entry_open_pwd2.delete(0, tk.END)
        self.entry_open_balance.delete(0, tk.END)
        self.entry_open_balance.insert(0, "0")

    # 通用：根据账号获取账户对象
    def get_account(self, acc_id):
        if acc_id not in self.accounts:
            return None
        return self.accounts[acc_id]

    # 查询余额
    def query_balance(self):
        acc_id = self.entry_op_id.get().strip()
        pwd = self.entry_op_pwd.get()

        if not acc_id or not pwd:
            self.show_info("账号和密码不能为空！", is_error=True)
            return

        account = self.get_account(acc_id)
        if not account:
            self.show_info(f"账号 {acc_id} 不存在！", is_error=True)
            return

        result = account.get_balance(pwd)
        if isinstance(result, str) and result == "密码错误":
            self.show_info("密码错误，无法查询余额！", is_error=True)
        else:
            self.show_info(f"账户 {acc_id} 当前余额为：{result}")

    # 存款
    def deposit(self):
        acc_id = self.entry_op_id.get().strip()
        pwd = self.entry_op_pwd.get()
        amount_str = self.entry_amount.get().strip()

        if not acc_id or not pwd:
            self.show_info("账号和密码不能为空！", is_error=True)
            return
        try:
            amount = float(amount_str)
        except ValueError:
            self.show_info("存款金额必须是数字！", is_error=True)
            return

        account = self.get_account(acc_id)
        if not account:
            self.show_info(f"账号 {acc_id} 不存在！", is_error=True)
            return

        result = account.deposit(pwd, amount)
        if "成功" in result:
            self.show_info(result)
        else:
            self.show_info(result, is_error=True)

    # 取款
    def withdraw(self):
        acc_id = self.entry_op_id.get().strip()
        pwd = self.entry_op_pwd.get()
        amount_str = self.entry_amount.get().strip()

        if not acc_id or not pwd:
            self.show_info("账号和密码不能为空！", is_error=True)
            return
        try:
            amount = float(amount_str)
        except ValueError:
            self.show_info("取款金额必须是数字！", is_error=True)
            return

        account = self.get_account(acc_id)
        if not account:
            self.show_info(f"账号 {acc_id} 不存在！", is_error=True)
            return

        result = account.withdraw(pwd, amount)
        if "成功" in result:
            self.show_info(result)
        else:
            self.show_info(result, is_error=True)

    # 修改密码
    def change_password(self):
        acc_id = self.entry_op_id.get().strip()
        old_pwd = self.entry_op_pwd.get()
        new_pwd = self.entry_new_pwd.get().strip()

        if not acc_id or not old_pwd or not new_pwd:
            self.show_info("账号、原密码、新密码都不能为空！", is_error=True)
            return

        account = self.get_account(acc_id)
        if not account:
            self.show_info(f"账号 {acc_id} 不存在！", is_error=True)
            return

        result = account.change_password(old_pwd, new_pwd)
        if "成功" in result:
            self.show_info(result)
            # 清空密码输入框（提高安全性）
            self.entry_op_pwd.delete(0, tk.END)
            self.entry_new_pwd.delete(0, tk.END)
        else:
            self.show_info(result, is_error=True)


# ====================== 主程序入口 ======================
if __name__ == "__main__":
    root = tk.Tk()
    app = BankSystemGUI(root)
    root.mainloop()