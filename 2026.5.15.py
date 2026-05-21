#os.walk()函数遍历的使用
# import os
# def visitdir(path):
#     for root, dirs, files in os.walk(path):
#         print(f"当前目录: {root}")
#         print(f"子文件夹: {dirs}")
#         print(f"文件: {files}")
# visitdir(r'c:\Users\Lenovo\Desktop\实训')
#编写一个程序，统计指定文件夹的大小以及文件和子文件夹的数量。
# import os
 
# def countdir(path):
#     # 计算指定路径下所有文件的总大小和文件及子文件夹的总数
#     size = 0
#     count = 0
#     for root, dirs, files in os.walk(path):
#         for f in files:
#             # 累加文件大小
#             size += os.path.getsize(os.path.join(root, f))
#             # 增加文件计数
#             count += 1
#         for d in dirs:
#             # 增加子文件夹计数
#             count += 1
#     return size, count
 
# size, count = countdir(r'c:\Users\Lenovo\Desktop\实训')
# print(f"文件夹大小为: {size} bytes")
# print(f"文件夹包含的文件和子文件夹的数量为: {count}")

# #可以继承python内置异常类来实现自定义的异常类
# class MyException(Exception):
#     def __init__(self, message):
#         self.message = message
#     def __str__(self):
#         return self.message
# #使用自定义的异常类
# try:
#     raise MyException("自定义异常")
# except MyException as e:
#     print(e)
# while True:
#     x=input('Please input:')
#     try:
#         x=int(x)
#         print('You have input {0}'.format(x))
#         break
#     except Exception as e:
#         print('Invalid input, please try again.')
# print('End of program.')


# from my_calc import jiafa,jianfa,chengfa,chufa
# a,b=map(float,input().split())
# c=input()
# if c=='+':
#     print(jiafa(a,b))
# elif c=='-':
#     print(jianfa(a,b))
# elif c=='*':
#     print(chengfa(a,b))
# elif c=='/'and b==0:
#     print("除数不能为0")
# else:
#     print(chufa(a,b))

#datetime函数库的基本使用
# import datetime
# #显示当前时间
# print(datetime.datetime.now())
# #显示指定日期的时间
# print(datetime.datetime(2021,1,1))
# #显示指定日期的时间戳
# print(datetime.datetime.timestamp(datetime.datetime(2021,1,1)))
# #显示指定日期的时间差
# print(datetime.datetime.now()-datetime.datetime(2021,1,1))
# #strftime()函数的使用
# print(datetime.datetime.now().strftime('%Y-%m-%d     %H:%M:%S'))

#生成随机六位验证码（包含数字和字母）
# import random
# import datetime
# def mima():
#     str=random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',k=6)
#     return ''.join(str)
# def shijian():
#     return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# if __name__ == "__main__":
#     code = mima()
#     time=shijian()
#     print(f"生成的验证码: {code}")
#     print(f"生成时间: {time}")
    
# import requests
# print("1")
#json的基本使用

#json字符串转字典
# json_str = '{"name": "John", "age": 30, "city": "New York"}'
# print(type(json_str))
# print(json_str)
# data = json.dumps(json_str)
# print(type(data))
# print(data)

import json
test={
"company": "Alibaba",
"employees": [{"name": "Alice", "position": "Engineer", "salary": 10000},
              {"name": "Bob", "position": "Manager", "salary": 15000}],
"location": "Hangzhou"}
aa=json.dumps(test)
print(aa)