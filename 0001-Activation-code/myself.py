 # coding=gbk

import random
import string


def randomOne():
    #随机生成一位大写字母
    s = ''
    for i in range(0,4):
        s = s+chr(random.randint(65,90))
    return s  #如果不写return语句，那么默认函数结尾会return None

sz = []
for i in range(0,200):
    sz = sz + [randomOne()]    #暂未考虑重复的随机四位大写字母

print(sz)