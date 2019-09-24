teacher = ['张三','李四','王五','赵六']
print(teacher[0])
#》》 张三
print(teacher[1])
#》》 李四
print(teacher[2])
#》》 王五
print(teacher[-1])
#》》 赵六 （倒数第一个）

print(teacher[:2])
#》》['张三','李四']
print(teacher[:-1])
#》》['张三','李四','王五']
print(teacher[1:])
#》》['李四','王五','赵六']
print(teacher[1:2])
#》》['李四']
print(teacher[1:-1])
#》》['李四','王五']

#增加元素
teacher.append('孙七')
print(teacher)
#》》['张三', '李四', '王五', '赵六', '孙七']

#删除元素 del 列表[偏移量]
del teacher[-1]
print(teacher)
#》》['张三', '李四', '王五', '赵六']

#

