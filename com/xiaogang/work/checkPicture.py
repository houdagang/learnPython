import cx_Oracle  # 引用模块cx_Oracle
import requests
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '不存在的图片'
sheet['A1'] = '路径'
sheet['B1'] = 'id'

conn = cx_Oracle.connect('hzz', 'sdslhzz_2017', '60.208.113.73:1522/bizdb')  # 连接数据库
print(conn.version)
c = conn.cursor()  # 获取cursor
# sql = 'select * from hzz_river_lyjg'
sql = "select nvl(SERVERPATH,'http://60.208.113.77:8081') || replace(MODULEID,'D:','') || TARGETFILENAME url,id from HZZ_COMMONS_FILE where STATUS = '0' and (SLTFLAG = '0' or SLTFLAG is null) and UPLOADFILETYPE in ('bmp','jpg','png','tif','gif','pcx','tga','exif','fpx','svg','psd','cdr','pcd','dxf','ufo','eps','ai','raw','WMF','webp','BMP','JPG','PNG','TIF','GIF','PCX','TGA','EXIF','FPX','SVG','PSD','CDR','PCD','DXF','UFO','EPS','AI','RAW','WEBP')"
x = c.execute(sql)  # 使用cursor进行各种操作
print(x)
rows = x.fetchall()  # 获取数据
# 打印数据
for row in rows:
    r = requests.get(row[0])
    if '4' in str(r.status_code):
        sheet.append([row[0], row[1]])

print('结束')
wb.save('D://统计不存在图片.xlsx')
wb.close()
x.fetchone()
c.close()  # 关闭cursor
conn.close()  # 关闭连接
