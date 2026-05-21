def jiafa(a,b):
    return a+b
def jianfa(a,b):
    return a-b
def chufa(a,b):
    return a/b
def chengfa(a,b):
    return a*b
a,b=map(float,input().split())
c=input()
if c=='+':
    print(jiafa(a,b))
elif c=='-':
    print(jianfa(a,b))
elif c=='*':
    print(chengfa(a,b))
elif c=='/'and b==0:
    print("除数不能为0")
else:
    print(chufa(a,b))