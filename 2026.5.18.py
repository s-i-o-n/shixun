#Requests库的使用
# import requests

# # url = "https://www.baidu.com"
# # response = requests.get(url)
# # a=response.json()
# # print(a)
# response = requests.get("https://httpbin.org/status/404/")
# print("状态码",response.status_code)
# try:
#     response.raise_for_status()
# except requests.exceptions.HTTPError as e:
#     print("请求出错",e)
# import requests
# try:
#     r=requests.get("https://httpbin.org/delay/1",timeout=1)
#     r.raise_for_status()
#     print("请求成功")
# except requests.exceptions.Timeout:
#     print("请求超时")
# except requests.exceptions.HTTPError as e:
#     print("请求出错",e)
'''
发送标准的httpget请求
检查响应码状态，是否成功
将服务器返回的内容解析为json格式
从解析的数据中提取并打印公网ip地址
编写完整的异常处理代码
'''
# import requests
# import json

# try:
#     response = requests.get("http://httpbin.org/ip")
#     response.raise_for_status()
#     data = json.loads(response.text)
#     ip = data["origin"]
#     print("公网ip地址为：", ip)
# except requests.exceptions.HTTPError as e:
#     print("请求出错", e)
# except requests.exceptions.Timeout:
#     print("请求超时")
# except json.JSONDecodeError as e:
#     print("解析json出错", e)
#高德API调用的基础使用
# import requests

# API_KEY = "fe3b492b1dc28ed2f600acdc963c83aa"
# import requests
# import json
# # 高德地理编码 API
# url = "https://restapi.amap.com/v3/geocode/geo"
# params = {
#     "key": "fe3b492b1dc28ed2f600acdc963c83aa",
#     "address": "新余",
#     "extensions":"all",
#     "output":"json"
# }
# # 发送请求
# response = requests.get(url, params=params)
# # 查看结果
# print(response.json())
# def get_ip_address():
#     try:
#         response = requests.get("http://httpbin.org/ip")
#         response.raise_for_status()
#         data = json.loads(response.text)
#         ip = data["origin"]
#         return ip
#     except requests.exceptions.HTTPError as e:
#         print("请求出错", e)
#     except requests.exceptions.Timeout:
#         print("请求超时")
#     except json.JSONDecodeError as e:
#         print("解析json出错", e)

# if __name__ == '__main__':
#     ip = get_ip_address()
#     print(ip)
#类和对象的基本了解
# class student:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#     def print_info(self):
#         print("姓名：", self.name)
#         print("年龄：", self.age)
#         print("成绩：", self.score)

# s = student("张三", 18, 90)
# b = student("李四", 19, 80)
# s.print_info()
# b.print_info()

#简单的类和对象的使用
# class Car:
#     def __init__(self, color="白色"):
#         self.color = color
#     def run(self):
#         print("一辆",self.color,"的汽车在跑")
# car1=Car()
# car2=Car()
# car1.run()
# car2.color="红色"
# car2.run()

# class Student:
#     school="新余学院"
#     def __init__(self,name):
#         self.name=name
#     def sex(self,gender):
#         self.gender=gender
#     def age(self,age):
#         self.age=age
# s1=Student("张三")
# s2=Student("李四")
# print(s1.name)
# print(s2.name)
# print(s1.name,s2.name)
# print(s1.school)
# print(Student.school)
# Student.school="清华大学" 
# print(s1.school,s2.school)
# s1.age(18)
# s1.sex("男")
# print(s1.age,s1.gender)

#定义一个带复杂方法的类
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def get_area(self):
#         return self.width * self.height
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)
#     #类方法的要点，必须使用装饰器
#     @classmethod
#     def create_square(cls,side):
#         return cls(side,side)
        
# r1 = Rectangle(5, 3)
# print(r1.get_area())
# print(r1.get_perimeter())
# r2=Rectangle.create_square(4)
# print(r2.get_area())

#三大特性
#封装
# class person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         if 0<age<150:
#             self.__age=age
#         else:
#             print("年龄不合法")
# p=person("张三",18)
# print(p.get_age())
# p.set_age(19)
# print(p.get_age())
# p.set_age(300)
# print(p.get_age())

#继承与多态的实战
#父类,含默认返回0的get_area()方法
# class Shape:
#     def __init__(self):
#         pass
#     def get_area(self):
#         return 0
# class Square(Shape):
#     def __init__(self, side):
#         super().__init__()
#         self.side = side
#     def get_area(self):
#         return self.side ** 2
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius
#     def get_area(self):
#         return 3.14 * self.radius ** 2

# # calculate_total_area 在类外部，不缩进
# def calculate_total_area(shapes):
#     total_area = 0
#     for shape in shapes:
#         total_area += shape.get_area()
#     return total_area

# # 实例化对象
# s1 = Square(5)
# c1 = Circle(3)
# print(s1.get_area())  # 输出: 25
# print(c1.get_area())  # 输出: 28.26
# shapes = [s1, c1]
# print(calculate_total_area(shapes))  # 输出: 5² + 3.14×3² = 25 + 28.26 = 53.26


#银行账户管理系统
'''
两个公开属性，account_id(账号)name(姓名)；两个私有属性，__balance(余额)和__password(密码)。
开户
查询余额
存款
取款
修改密码
'''
#开户
class BankAccount:
    def __init__(self, account_id, name, password, balance=0):
        self.account_id = account_id
        self.name = name
        self.__password = password
        self.__balance = balance
    
    # 开户（设置初始密码）
    def open_account(self):
        print(f"开户成功！账号：{self.account_id}，姓名：{self.name}")
    # 查询余额
    def query_balance(self):
        password = input("请输入密码：")
        if password == self.__password:
            print(f"密码正确，账户余额为：{self.__balance}")
        else:
            print("密码错误，无法查询余额")
    # 存款
    def deposit(self):
        password = input("请输入密码：")
        if password == self.__password:
            amount = float(input("请输入存款金额："))
            if amount <= 0:
                print("存款金额必须大于0")
            else:
                self.__balance += amount
                print(f"存款成功，账户余额为：{self.__balance}")
        else:
            print("密码错误，无法存款")
    # 取款
    def withdraw(self):
        password = input("请输入密码：")
        if password == self.__password:
            amount = float(input("请输入取款金额："))
            if amount <= 0:
                print("取款金额必须大于0")
            elif self.__balance < amount:
                print("余额不足")
            else:
                self.__balance -= amount
                print(f"取款成功，账户余额为：{self.__balance}")
        else:
            print("密码错误，无法取款")
    # 修改密码
    def change_password(self,new_password):
        password=input("请输入当前密码：")
        if password==self.__password:
            new_password=input("请输入新密码：")
            self.__password=new_password
            print("密码修改成功！")
        else:
            print("密码错误！")
#实例化对象
account1 = BankAccount("123456", "张三", "123456")
account1.open_account()
account1.query_balance()
account1.deposit()
account1.withdraw()
account1.change_password("<PASSWORD>")
account1.query_balance()

