# ls = ['apple', 'banana', 'orange', 'pear']
# for i, j in enumerate(ls, start=1):
#     print(f"{i}: {j}")

# s=input("请输入对应的水果：")
# if s in ls:
#     print(f"{s}在列表中，位置为{ls.index(s)+1}")
# else:
#     print(f"{s}不在列表中")
# import random
# def sub(x):
#     return x*x
# ls=[random.randint(1,10) for i in range(5)]
# print(ls)
# print(list(map(sub,ls)))
# ls=[i for i in range(1,11)]
# print(ls)
# result=filter(lambda x:x%2==1,ls)
# print(list(result))
# ls=[1,-2,3,-4,5,-6,7,-8,9,-10]
# ls1=list(filter(lambda x:x>0,ls))
# print(ls1)
# print(list(map(lambda x:x*2,ls1)))

# xueke = ['语文', '数学', '英语']
# # 多组学生成绩
# students = [
#     {'姓名': '张三', '成绩': [80, 90, 85]},
#     {'姓名': '李四', '成绩': [55, 72, 68]},
#     {'姓名': '王五', '成绩': [95,100, 92]},
# ]
# def avg(x):
#     return sum(x) / len(x)
# def zongfen(x):
#     return sum(x)
# for stu in students:
#     name = stu['姓名']
#     chengji = stu['成绩']
#     print(f"\n{name}的成绩：")
#     s = zip(xueke, chengji)
#     for i, j in s:
#         if j >= 85:
#             print(f"  {i}: {j} 优秀")
#         elif j >= 60:
#             print(f"  {i}: {j} 及格")
#         else:
#             print(f"  {i}: {j} 不及格")
#     print(f"  平均分: {avg(chengji):.2f}")
#     print(f"  总分: {zongfen(chengji)}")
# for stu in students:
#     name = stu['姓名']
#     chengji = stu['成绩']
#     s = zip(xueke, chengji)
#     print(f"{name}最高分学科: {max(s, key=lambda x: x[1])}")

# print("\n各学科最高分：")
# for idx, subj in enumerate(xueke):
#     top = max(students, key=lambda stu: stu['成绩'][idx])
#     print(f"  {subj}最高分: {top['姓名']} ({top['成绩'][idx]}分)")

# while True:
#     n = input("请输入一个学生的成绩：")
#     if not n.isdigit():
#         print("输入错误，请重新输入")
#         continue
#     n = int(n)
#     if 90 <= n <= 100:
#         print("该学生成绩优秀A")
#     elif 60 <= n < 90:
#         print("该学生成绩及格B")
#     elif 0 <= n < 60:
#         print("该学生成绩不及格C")
#     else:
#         print("输入错误，请重新输入")


# def qq(x):
#     if x=='yes':
#         return True
#     elif x=='no':
#         return False
#     else:
#         print("输入错误，请重新输入")
# ls=[]
# while True:
#     n=int(input("请输入一个学生的成绩："))
#     ls.append(n)
#     print(sum(ls)/len(ls))
#     m=input("是否继续输入？(yes/no)")
#     if qq(m):
#         continue
#     else:
#         break

# def qq(x):
#     if x == 'yes':
#         return True
#     elif x == 'no':
#         return False
#     else:
#         print("输入错误，请重新输入")
#         return None   # 明确返回 None，让调用方处理
# ls = []
# while True:
#     # 安全获取成绩（支持整数，可扩展为浮点数）
#     try:
#         n = int(input("请输入一个学生的成绩："))
#     except ValueError:
#         print("输入错误，请输入一个整数成绩")
#         continue

#     ls.append(n)
#     print(f"当前平均分：{sum(ls)/len(ls)}")

#     while True:   # 内层循环确保必须输入 yes 或 no
#         m = input("是否继续输入？(yes/no)：")
#         result = qq(m)
#         if result is None:
#             continue   # 重新询问
#         elif result:
#             break       # 跳出内层循环，继续外层循环（continue 的效果在外层体现）
#         else:
#             print("结束输入")
#             exit()     # 或者 break 外层循环（需要标记）


# for i in range(1,10):
#     print(i)


# for i in range(100, 1, -1):
#     is_prime = True
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("100以内的最大素数是:", i)
#         break

# for i in range(1,101):
#     if i%5!=0 and i%7==0:
#         print(i)
# for num in range(100, 1000):
#     a = num // 100          
#     b = (num // 10) % 10    
#     c = num % 10            
#     if a**3 + b**3 + c**3 == num:
#         print(num)

# def find_narcissistic_numbers(n):
#     # 计算n位数的范围
#     lower_bound = 10**(n-1)
#     upper_bound = 10**n
#     narcissistic_numbers = []
#     for number in range(lower_bound, upper_bound):
#         # 将数字转换为字符串，以便逐位处理
#         digits = str(number)
#         # 计算每个位上的数字的n次幂之和
#         sum_of_powers = sum(int(digit) ** n for digit in digits)
#         # 如果这个和等于原数字，则是水仙花数
#         if sum_of_powers == number:
#             narcissistic_numbers.append(str(number))
#     return narcissistic_numbers
# # 示例用法：找出所有3位水仙花数
# n = 3
# result = find_narcissistic_numbers(n)
# print(f"所有{n}位水仙花数为: {result}")

#求n位数的水仙花数
# n=int(input("请输入一个整数："))
# for num in range(10**(n-1),10**n):
#     if sum(map(lambda i:int(i)**n,str(num)))==num:
#         print(num)


import random
ls=[random.randint(1,1000) for i in range(20)]
print(ls)
ls2=ls[::2]
print(ls2)
ls2.sort()
print(ls2)  