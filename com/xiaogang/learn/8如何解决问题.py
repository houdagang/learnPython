#合并列表
A=[91, 95, 97, 99]
B=[92, 93, 96, 98]
A.extend(B)
print(A)

#排序
#sorted 生成一个排序后的新序列，不动原来的序列
C = sorted(A)
print(C)
print(A)
#sort给原序列排序
A.sort()
print(A)
