import math


def A(a,b):
    print("第一个参数的值为"+str(a))
    print("第一个参数的值为"+str(b))

a = 1
b = 2
A(b,a)
#第一个参数的值为2
#第二个参数的值为1

#格式化字符
#%f的意思是格式化字符为浮点型，%.1f的意思是格式化字符为浮点型，并保留1位小数（四舍五入）
a1 = 2.3333
a2 = 4.4567
print('a1的值保留一位是：%.1f'%a1)
print('a2的值保留三位是：%.3f'%a2)

#math模块 import math
#math.ceil() 将得出来的数值向上取整
print(math.ceil(a1))
#3

#return
#带有return时，打印或变量接收，获得返回值
def B():
    b1 = 1
    b2 = 2
    return b1,b2
print(B())
print(type(B()))
#(1,2)
#<class 'tuple'>

#元组 tuple
#元组和列表类似，不同之处在于元组的元素不能修改。元组使用() 列表使用[]
#元组的创建
tup1 = (1,2,3,4,5)
#不需要括号也可以
tup2 = 1,2,3,4,5
tup3 = "a","b","c"
print(tup1)
print(type(tup1))
print(tup2)
print(type(tup2))
print(tup3)
print(type(tup3))
#(1, 2, 3, 4, 5)
#<class 'tuple'>
#(1, 2, 3, 4, 5)
#<class 'tuple'>
#('a', 'b', 'c')
#<class 'tuple'>

#创建空元祖 
tup4 = ()
#元组的访问类似列表
print("tup1[0]:",tup1[0])
print("tup2[1:5]:",tup2[1:5])
#tup1[0]: 1
#tup2[1:5]: (2, 3, 4, 5)

#元组中的元素值虽然不能修改，但是可以进行元组的连接
tup5 = tup2 + tup3
print(tup5)
#(1, 2, 3, 4, 5, 'a', 'b', 'c')

#同样的，虽然不能删除元素，但是可以整个删除
del tup5
print("删除后的元组：")
#print(tup5)
#NameError: name 'tup5' is not defined

#基本的元组运算符及内置函数
print(len(tup1))
print(tup3*3)
#5
#('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

#迭代
for i in tup2:
    print(i)
#1  2  3  4  5
print(max(tup3))
print(min(tup2))
print(tuple([1,2,3]))
#c
#1
#(1, 2, 3)