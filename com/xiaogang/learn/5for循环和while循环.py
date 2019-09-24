
#for ... in ...
for i in [1,2,3,4,5]:
    print(i)
#1
#2
#3
#4
#5

#遍历字典
a = {1:'张三',2:'李四',3:'王五'}
for a,b in a.items():
    print(str(a) + ':' + str(b))
#1:张三
#2:李四
#3:王五

#遍历键值（一）
b = {1:'张三',2:'李四',3:'王五'}
for i in b:
    print(i)
#1
#2
#3

#遍历键值（二）
c = {1:'张三',2:'李四',3:'王五'}
for i in c.keys():
    print(i)
#1
#2
#3

#遍历字典的值(一)
d = {1:'张三',2:'李四',3:'王五'}
for i in d.values():
    print(i)
#张三
#李四
#王五

#遍历字典的值（二）
e = {1:'张三',2:'李四',3:'王五'}
for i in e:
    print(e[i])

#range() 函数
#不带间隔
for i in range(1,4):
    print(i)
#1
#2
#3

#带间隔
for i in range(1,10,2):
    print(i)
#1
#3
#5
#7
#9 

#while循环
a1=1
while a1<4:
    print(a1*5)
    a1=a1+1
#5
#10
#15

#while...else...
a2=input('你是不是傻？')
while a2 == '是':
    print('诚实可信')
else:
    print('还狡辩')

#你是不是傻？不是
#还狡辩

#避免死循环的方法
#1
#exit() 括号里面加入自己退出程序的打印说明，但是python3要加引号
#while True:
#    print(1)
#    exit("退出循环")
#2 终端区按 ctrl+c，强行结束运行
#3 代码去使用break语句
while True:
    print(123)
    break

#延伸 pop()函数
mw = ['钢铁侠','美国队长','奇异博士','蝙蝠侠','蜘蛛侠']
dc = []
del_a=mw.pop(3)
dc.append(del_a)
print(mw)
print(dc)
#['钢铁侠', '美国队长', '奇异博士', '蜘蛛侠']
#['蝙蝠侠']