import datetime

#工作日数组
def getGzsc():
    #当前年
    year = datetime.datetime.now().year
    #当前月
    month = datetime.datetime.now().month
    like_ny = str(year)[2:] + '-' + str(month) + '-'
    #工作日数组
    gzr_sz = ['19-11-08']
    gzr = 0
    for i in gzr_sz:
        if like_ny in i:
            gzr = gzr + 1
    return gzr * 7.5

#基本工资
def getGz():
    gz = 0
    try:
        gz = int(input('请输入你的基本工资:'))
    except:
        print('请输入正整数')
        getGz()
    else:
        return gz

#加班时长
def getJbsc():        
    jbsc = 0.0
    try:
        jbsc = float(input('请输入本月的加班时长:'))    
    except:
        print('请输入小数或整数')
        getJbsc()
    else:
        return jbsc

#理论每小时的加班费
def getJbf():        
    jbf = 0.0
    try:
        jbf = float(input('请输入理论上的加班费:'))    
    except:
        print('请输入小数或整数')
        getJbf()
    else:
        return jbf

def main():
    ll_gzsc = getGzsc()#理论本月工作时长
    gz = getGz()#工资
    jbsc = getJbsc()#加班时长
    jbf = getJbf()#每小时的加班费
    ll_hour_gz = gz/ll_gzsc #理论上每小时的工资
    print("理论上本月每小时的工资是：" + str(ll_hour_gz))
    sj_hour_gz = (gz + jbsc * jbf)/(ll_gzsc + jbsc)
    print("实际上本月每小时的工资是：" + str(sj_hour_gz))
    ll_gz = ll_hour_gz * (ll_gzsc + jbsc)
    print("如果将按正常工作时间来算加班的话，你的工资应该是：" + str(ll_gz))
    ll_ts = ll_gz/ll_hour_gz/7.5
    print("换算成正常工作日应该是"+ str(ll_ts) + '天')
    
    
main()