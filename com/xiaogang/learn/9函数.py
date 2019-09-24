#函数定义
#dev 函数名(参数1，参数2,....):
#   函数体
#   return 语句
def func1():
    print(1)
    return 1
def func2():
    print(2)

a = func1()
print(a)
b = func2()
print(b)
#1
#1
#2
#None

#默认参数
def menu(appetizer,course,dessert='绿豆沙'):
    print('一份开胃菜：'+ appetizer)
    print('一份主食:'+ course)
    print('一份甜品：'+ dessert)
menu('话梅花生','牛肉拉面')
#一份开胃菜：话梅花生
#一份主食:牛肉拉面
#一份甜品：绿豆沙
menu('话梅花生','牛肉拉面','银耳蛋花粥')
#一份开胃菜：话梅花生
#一份主食:牛肉拉面
#一份甜品：银耳蛋花粥


def menu1(appetizer,course,*barbeque,dessert='绿豆沙'):
    print('一份开胃菜：'+appetizer)
    print('一份主菜：'+course)
    print('一份甜品：'+dessert)
    for i in barbeque:
        print('一份烤串：'+i)
        
menu1('话梅花生','牛肉拉面','烤鸡翅','烤茄子','烤玉米',dessert='银耳羹')
#一份开胃菜：话梅花生
#一份主菜：牛肉拉面
#一份甜品：银耳羹
#一份烤串：烤鸡翅
#一份烤串：烤茄子
#一份烤串：烤玉米
menu1('话梅花生','牛肉拉面','烤鸡翅','烤茄子')
#一份开胃菜：话梅花生
#一份主菜：牛肉拉面
#一份甜品：绿豆沙
#一份烤串：烤鸡翅
#一份烤串：烤茄子

def menu2(appetizer,course,*barbeque,dessert):
    print('一份开胃菜：'+appetizer)
    print('一份主菜：'+course)
    print('一份甜品：'+dessert)
    for i in barbeque:
        print('一份烤串：'+i)
#menu2('话梅花生','牛肉拉面','烤鸡翅','烤茄子')
#TypeError: menu2() missing 1 required keyword-only argument: 'dessert'

#局部变量
def A():
    a='张三'
    print(a)

name='李四'
def B():
    print(name)
B()
#李四

def C():
    global num
    num = 5
C()
print(num)
#5

#list()函数
n = '张三'
n = list(n)
print(n)
#['张', '三']

#reversed()函数
#参数是列表1：
a1=[1,2,3,4,5]
b1=reversed(a1)
print(a1)
#结果显示为：
#[1, 2, 3, 4, 5]
print(b1)
#结果显示为：
#<list_reverseiterator object at 0x0000024F76DC0A90>
for i in b1:#第一次遍历
    print(i)
#结果显示为：
#5 4 3 2 1
for i in b1:#第二次遍历为空
    print(i)
#结果显示为：啥也没有