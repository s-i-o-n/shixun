# #随机字符串的练习
# a='jfdsijgdio'
# print(a)
# print(a.find('j')) #查找字符串中第一个出现的i的位置
# print(a.index('i')) #查找字符串中第一个出现的i的位置，如果没有找到，会报错
# print(a.count('i')) #统计字符串中出现的i的次数
# print(a.rfind('j'))#从右往左找第一个出现的j的位置
# print(a.rindex('i'))#从右往左找第一个出现的i的位置，如果没有找到，会报错
# print(a.replace('j','k'))#把字符串中的j替换为k
# print(a.split('i'))#把字符串以i为分隔符分割成列表
# print(a.join(['a','b','c']))#把列表用i连接成字符串

# #字符串的常用方法
# text='''helloworld'''
# # 遍历字符串中的每个字符及其索引
# for index,ch in enumerate(text):
#     # 检查当前索引是否为字符第一次出现的索引
#     if index==text.index(ch):
#         # 打印字符及其首次出现的索引，不换行
#         print((index,ch),end='')
#         print((text.count(ch),ch))

#字符串的常用方法
# text='heallobworccld'
# # 使用 split 方法按指定字符分割字符串
# print(text.split('l'))
# # 使用 rsplit 方法按指定字符从右向左分割字符串
# print(text.rsplit('l'))
# # 使用 partition 方法按指定字符分割字符串，返回分割后的三部分
# print(text.partition('l'))
#maketrans方法用于创建字符映射表，用于替换字符串中的字符
# table=str.maketrans('abc','123')
# print(text.translate(table))#把字符串中的a替换为1，b替换为2，c替换为3
# #使用replace方法替换字符串中的字符
# print(text.replace('l','gg'))#把字符串中的l替换为L


# text='hello world! I like python. this is a nice day. right?'
# def count_text(text):
#     # 统计字符串中每个单词出现的次数,清除标点符号
#     text=text.lower().replace('.','').replace('!','').replace('?','')
#     # 按空格分割字符串，得到单词列表
#     print(text)
#     words=text.split()
#     # 统计单词出现的次数
#     count_dict={}
#     for word in words:
#         if word in count_dict:
#             count_dict[word]+=1
#         else:
#             count_dict[word]=1
#     # 返回单词出现的次数
#     return count_dict
# print(count_text(text))
# print(len(count_text(text)))

# text='hello world! I like python. this is a nice day. right?'
# def juzi(test):
#     ls=[]
#     start = 0
#     end=0
#     for i in test:
#         if i == '!' or i == '.' or i == '?':
#             ls.append(test[start:end+1])
#             start = end+1
#         end += 1      
#     return ls
# print(juzi(text))

#strip()函数使用示例
# text='   hello world   '
# print(text.strip())#去除两端空格
# print(text.lstrip())#去除左侧空格
# print(text.rstrip())#去除右侧空格
# test='adcbbbccddeeefffg'
# print(test.strip('abc'))#去除指定字符的空格
# print(test.strip('defg'))#去除指定字符的空格

# text='''姓名：张三
# 性别:男
# 年龄25    
# 爱好:游泳
# '''
# info=text.split('\n')
# print(info)
# for i in info:
#     print(i[:2],i[2:].strip(':'),sep=':')


# import string
# # 打印数字字符
# print(string.digits)
# # 打印字母字符（包括大小写）
# print(string.ascii_letters)
# # 打印标点符号字符
# print(string.punctuation)



#文件的写入操作示例
# s='高捷是大帅哥、段浩宇也是大帅哥。'
# with open('test.txt','w',encoding='utf-8') as f:
#     f.write(s)   # 写入字符串
#     f.write('\n') # 写入换行符
#     f.write(str(123)) # 写入数字
#     f.write('\n') # 写入换行符
#     f.write(str(3.14)) # 写入数字
#     f.write('\n') # 写入换行符
#     f.write(str(True)) # 写入布尔值
#     f.write('\n') # 写入换行符
#     f.write(str(False)) # 写入布尔值
#     f.write('\n') # 写入换行符
#     f.write(str(['apple','banana','orange'])) # 写入列表
#     f.write('\n') # 写入换行符
#     f.write(str(('apple','banana','orange'))) # 写入元组
#     f.write('\n') # 写入换行符
#     f.write(str({'apple':100,'banana':200,'orange':300})) # 写入字典
#     f.write('\n') # 写入换行符
#将文本内的内容升序排序

with open('test.txt', 'r+', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]  # 去除每行末尾的换行符
    lines.sort(key=lambda x: int(x))  # 按整数升序排序
    lines = [line + '\n' for line in lines]  # 重新添加换行符
    f.seek(0)  # 移动文件指针到文件开头
    f.writelines(lines)  # 将排序后的行写回文件
    f.truncate()  # 截断文件多余的内容
