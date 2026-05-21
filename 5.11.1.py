# import random
# a=random.randint(100,10000)
# print(a)
# a=str(a)
# for i in a[::-1]:
#     print(i,end=' ')

# print()
# import math
# a,b=map(int,input().split())
# c=math.sqrt(a*a+b*b)
# print(c)
#直接三角形
# a,b=map(float,input().split())
# c=(a*a+b*b)**0.5
# print(c)



#任意输入三个英文单词，按字典顺序输出
# s=input().split()
# s.sort()
# print(' '.join(s))
# s = input("x,y,z: ").split(',')
# x, y, z = s[0].strip(), s[1].strip(), s[2].strip()

# # 冒泡式排序：确保 x <= y <= z
# if x > y:
#     x, y = y, x
# if y > z:
#     y, z = z, y
# if x > y:
#     x, y = y, x

# print(x, y, z)

  
# print(ord('a'))
# print(ord('A'))
# print(ord('z'))
# print(ord('Z'))

str=input()
a=''
for i in str:
    if ord(i)>=97 and ord(i)<=122:
        i=chr(ord(i)-32)
    else: 
        i=chr(ord(i)+32)
    a+=i
print(a)
