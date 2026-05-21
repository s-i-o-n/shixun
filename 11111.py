class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        return f"书名：{self.title}，作者：{self.author}，价格：{self.price}元"


class BankAccount:
    def __init__(self, account_id, name, password, balance=0):
        self.account_id = account_id
        self.name = name
        self.__password = password
        self.__balance = balance

    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            return "密码错误"

    def deposit(self, password, amount):
        if password != self.__password:
            return "密码错误"
        if amount <= 0:
            return "存款金额必须大于0"
        self.__balance += amount
        return f"存款成功，当前余额：{self.__balance}"

    def withdraw(self, password, amount):
        if password != self.__password:
            return "密码错误"
        if amount <= 0:
            return "取款金额必须大于0"
        if self.__balance < amount:
            return "余额不足"
        self.__balance -= amount
        return f"取款成功，当前余额：{self.__balance}"

    def change_password(self, old_password, new_password):
        if old_password != self.__password:
            return "原密码错误"
        self.__password = new_password
        return "密码修改成功"

    def get_info(self):
        return f"账号：{self.account_id}，姓名：{self.name}"

    def calc_interest(self, years=1):
        return self.__balance * 0.015 * years


if __name__ == "__main__":
    print("=== 作业一：Book类测试 ===")
    b = Book("三体", "刘慈欣", 68.00)
    print(b.show_info())

    print("\n=== 作业二：BankAccount类测试 ===")
    acc = BankAccount("001", "张三", "123456", 10000)
    print(acc.get_info())
    print(f"当前余额：{acc.get_balance('123456')}")
    print(f"存款：{acc.deposit('123456', 5000)}")
    print(f"1年利息：{acc.calc_interest(1)}")
    print(f"3年利息：{acc.calc_interest(3)}")
