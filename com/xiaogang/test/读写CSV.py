import csv
#文件位置，操作模式，避免两倍行距，编码格式
csv_file = open('d://demo.csv','w',newline='',encoding='gbk')
#创建writer对象
writer = csv.writer(csv_file)
#随便想写点
writer.writerow(['电影','豆瓣评分'])
writer.writerow(['银河护卫队','8.0'])
#在csv文件里写入一行文字 “银河护卫队”和“8.0”。
writer.writerow(['复仇者联盟','8.1'])
#在csv文件里写入一行文字 “复仇者联盟”和“8.1”。
csv_file.close()

csv_file_read=open('d://demo.csv','r',newline='',encoding='gbk')
reader=csv.reader(csv_file_read)
for row in reader:
    print(row)
csv_file_read.close()