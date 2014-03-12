# -*- coding:utf-8 -*-
import random
from netaddr import *

f = open('ribascii', 'r')
pfxs = []
dest = []

for line in f.readlines():
    if line.split(': ')[0] == '|ANNOUNCE':
        pfx = line.split(': ')[1].split('/')[0] 
        leng = int(line.split(': ')[1].split('/')[1])
        if leng < 32 or leng > 64:
            continue
        
        if pfx in pfxs:#same prefix appear again
            continue
        pfxs.append(pfx)

        random.seed()
        ip6 = IPAddress(pfx) + random.getrandbits(128-leng)
        dest.append(ip6)

f.close()

