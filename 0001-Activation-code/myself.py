 # coding=gbk

import random
import string


def randomOne():
    #�������һλ��д��ĸ
    s = ''
    for i in range(0,4):
        s = s+chr(random.randint(65,90))
    return s  #�����дreturn��䣬��ôĬ�Ϻ�����β��return None

sz = []
for i in range(0,200):
    sz = sz + [randomOne()]    #��δ�����ظ��������λ��д��ĸ

print(sz)