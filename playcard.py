def f1(x,y):
    return x+y

def f2(f,a,b):
    return f(a)+b
b=5
c=7
v=f2(lambda num:f1(num,num),c,b)
print(v)


# a = [3,4,3,1,1,2,5,4,3]
# slow,fast = 0,0
# s=set()
# while fast<len(a):
#     if a[fast] in s:
#         fast+=1
#     else:
#         s.add(a[fast])
#         a[slow]=a[fast]
#         slow+=1
# print(slow)
# print(a[:slow])