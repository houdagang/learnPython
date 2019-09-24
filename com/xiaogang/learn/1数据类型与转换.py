#字符拼接
name = '张三'
print('姓名：' + name)
# > > 姓名：张三

#type函数
print(type(1))
# 》 》 <class 'int'>
print(type(1.5))
# 》 》 <class 'float'>
print(type('张三'))
# 》 》 <class 'str'>

#str() 函数
num1 = 123
num2 = 1.55
print(type(num1))
print(type(num2))
print(type(str(num1)))
print(type(str(num2)))
# 》 》<class 'int'>
# 》 》<class 'float'>
# 》 》<class 'str'>
# 》 》<class 'str'>

#int() 函数
str1 = '11'
flo1 = 1.9
str2 = '张三'
str3 = '1.1'
print(int(str1))
# 》 》 11
#print(int(str2)) 报错
#print(int(str3)) 报错
print(int(flo1)) #(截取整数部分)
# 》 》 1

#float函数
print(float('1.1'))
# 》 》 1.1
print(float(1))
# 》 》 1.0
#print(float('张三')) #报错