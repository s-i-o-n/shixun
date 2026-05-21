'''
列表的增删改查
增:append()、insert()、extend()
删:pop()、remove()
改:sort()、reverse()、sort(reverse=True)
查:index()、count()、len()
'''
# import random
# # 生成一个包含10个1到100之间随机整数的列表
# ls=[random.randint(1,100) for i in range(10)]
# print(ls)
# # 从用户输入获取一个数字并将其添加到列表中
# a=int(input("请输入一个数字："))
# ls.append(a)
# print(ls)
# # 将另一个列表ls1中的元素添加到ls的末尾
# ls1=[1,2,3]
# ls.extend(ls1)
# print(ls)
# # 在列表的索引2位置插入数字4
# ls.insert(2,4)
# print(ls)
# # 移除列表中的最后一个元素
# ls.pop()
# print(ls)
# # 移除列表中第一个值为4的元素
# ls.remove(4)
# print(ls)
# # 对列表进行升序排序
# ls.sort()
# print(ls)
# # 反转列表中的元素顺序
# ls.reverse()
# print(ls)
# # 对列表进行降序排序
# ls.sort(reverse=True)
# print(len(ls))
# # 从用户输入获取一个数字并输出其在列表中的索引
# z=input("请输入要查找的数字：")
# print(ls.index(int(z)))
# # 从用户输入获取一个数字并输出其在列表中出现的次数
# print(ls.count(int(z)))




# ls=[]
# while True:
#     a=input("请输入：")
#     if a=="exit":
#         break 
#     else:
#         ls.append(a)
#         continue
# ls1=list(reversed(ls))
# print(ls1)

'''
字典的使用方法
'''
# ls1=[1,2,3,4,5]
# ls2=['a','b','c','d','e']
# # 合并两个列表为字典
# d=dict(zip(ls1,ls2))
# print(d)
# # 字典的键值对添加
# d[6]='f'
# print(d)
# # 字典的键值对删除
# del d[6]
# print(d)
# # 字典的键值对修改
# d[2]='g'
# print(d)
# # 字典的键值对查找
# print(d.get(3))
# #
# print(d.items())


# students = [
#     {'学号':'001','姓名': '张三', '成绩': '90'},
#     {'学号':'002','姓名': '李四', '成绩': '72'},
#     {'学号':'003','姓名': '王五', '成绩': '100'}]
students1={'001':{'姓名': '张三', '性别': '男','联系方式':'11111111111'}
           ,'002':{'姓名': '李四', '性别': '女','联系方式':'33333333333'}
           ,'003':{'姓名': '王五', '性别': '男','联系方式':'22222222222'}
           }
#打印学生所有信息
def print_student_info(students1):
    for student_id, info in students1.items():
        print(student_id, info['姓名'], info['性别'], info['联系方式'])
# 根据学号输出性别
def get_student_gender(students1, student_id):
    if student_id in students1:
        return students1[student_id]['性别']
    else:
        return "学号不存在！"
    
def add_student_info(students1):
    student_id = input("请输入学号：")
    student_name = input("请输入姓名：")
    student_gender = input("请输入性别：")
    student_contact = input("请输入联系方式：")
    students1[student_id] = {'姓名': student_name, '性别': student_gender, '联系方式': student_contact}
    print("添加成功！")
def delete_student_info(students1):
    student_id = input("请输入学号：")
    if student_id in students1:
        del students1[student_id]
        print("删除成功！")
    else:
        print("学号不存在！")
def update_student_info(students1):
    student_id = input("请输入学号：")
    if student_id in students1:
        student_name = input("请输入姓名：")
        student_gender = input("请输入性别：")
        student_contact = input("请输入联系方式：")
        students1[student_id] = {'姓名': student_name, '性别': student_gender, '联系方式': student_contact}
        print("修改成功！")
    else:
        print("学号不存在！")
#根据性别筛选学生
def filter_student_by_gender(students1, gender):
    result = []
    for student_id, info in students1.items():
        if info['性别'] == gender:
            result.append((student_id, info))   # 存储学号和信息
    return result

while True:
    print("1. 打印学生信息")
    print("2. 根据学号查询学生性别")
    print("3. 退出")
    print("4. 添加学生信息")
    print("5. 删除学生信息")
    print("6. 修改学生信息")
    print("7. 根据性别筛选学生")
    choice = input("请输入选项：")
    if choice == "1":
        print_student_info(students1)
    elif choice == "2":
        student_id = input("请输入学号：")
        print(get_student_gender(students1, student_id))
    elif choice == "3":
        break
    elif choice == "4":
        add_student_info(students1)
    elif choice == "5":
        delete_student_info(students1)
    elif choice == "6":
        update_student_info(students1)
    elif choice == "7":
        gender = input("请输入性别：")
        result = filter_student_by_gender(students1, gender)
        for student_id, info in result:
            print(student_id, info['姓名'], info['性别'], info['联系方式'])
    else:
        print("输入错误！")

# def demo(newitem,old_list=[]):
#     old_list.append(newitem)
#     return old_list
# print(demo('5',[1,2,3]))
# print(demo('aaa',['a','b']))
# print(demo('a'))
# print(demo('b'))