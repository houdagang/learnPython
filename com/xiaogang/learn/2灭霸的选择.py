#单相判断 if
a = -3
if a >= 6:
    print('你拥有无穷的力量')
# 》》如果变量a大于等于6，输出你拥有无穷的力量，否则，不输出

#双向判断 if...else...
if a >= 6:
    print('大于等于6')
else:
    print('小于6')
#》》如果变量a 大于等于6，输出大于等于6，否则，输出小于6

#多向判断 if...elif...else
if a >= 4:
    print('大于等于4')
elif a == 3:
    print('等于3')
elif a == 2:
    print('等于2')
else:
    print('小于等于1')
#》》elif 可以写多个

#嵌套使用
historyscore=26
if historyscore>=60:   
    print('你已经及格')
    if historyscore>=80:
        print('你很优秀')
    else:
        print('你只是一般般')
else:
    print('不及格')
    if historyscore<30:
        print('学渣')
    else:
        print('还能抢救一下')
print('程序结束')