import requests
import openpyxl


wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '水发答案'
sheet['A1'] = 'id'
sheet['B1'] = '题目'
sheet['C1'] = '答案'

tk = []
for i in range(100):
    res = requests.post('https://www.njsfly.com.cn/wechat/queryWTList')
    json = res.json()
    list = json['allpro']['prolist'][0]
    for tm in list:
        id = tm['guid']
        name = tm['wtbt']
        da = tm['option']
        zqda = ''
        for j in da:
            if j['sfzqda'] == '1':
                zqda = zqda + ',' + j['xxbt']
        zqda = zqda[1:]
        sheet.append([id,name,zqda])
wb.save('d://答案.xlsx')
wb.close()
print('结束')