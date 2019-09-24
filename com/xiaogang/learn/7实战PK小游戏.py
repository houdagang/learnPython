import time,random
player_life = random.randint(100,150)
player_attack = random.randint(30,50)
enemy_life = random.randint(100,150)
enemy_attack = random.randint(30,50)

print('【玩家】\n血量:'+str(player_life) + '\n攻击:'+str(player_attack))
print("---------------------------")
time.sleep(1)
print('【敌人】\n血量:'+str(enemy_life) + '\n攻击:'+str(enemy_attack))
print("---------------------------")
time.sleep(1)

while (player_life > 0) and (enemy_life > 0):
    player_life = player_life - enemy_attack 
    enemy_life = enemy_life - player_attack 
    print('你发起了攻击，【敌人】剩余血量'+str(enemy_life))
    #player_life是整数，所以拼接时要先用str()转换
    print('敌人向你发起了攻击，【玩家】剩余血量'+str(player_life))
    print('------------------------')
    time.sleep(1.5)


#%d %f %s
a = 123.12
print('%d'%a)
#123
print('%s'%a)
#123.12

#format
a=2
b='二'
print('我听{}泉映月听了{}次'.format(b,a))
#我听二泉映月听了2次
print('我听{1}泉映月听了{0}次'.format(a,b))
#我听二泉映月听了2次

#下面的随机数只能从1,3,5,7，。。。97,99中取值
print(random.randrange(1,100,2))

#random.choice()
#下面的函数会从python中随机选取一个字母
print(random.choice('python'))

#random.shuffle(a)
#将序列a中的元素打乱
s = [1,2,3,4,5,6]
random.shuffle(s)
print(s)
#[3, 4, 1, 2, 5, 6]

#random.sample(x,y)
#从x中随机抽取y个随机数字(y不能大于x的长度)
print(random.sample('python',5))
#['p', 't', 'n', 'h', 'y']
print(random.sample(range(0,32),7))