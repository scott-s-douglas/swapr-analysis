import sqlite3 as lite
import sys
import glob
import os.path
import random
from itertools import combinations

con = lite.connect('.\AnonymousS2014Campus.sqlite')
cur = con.cursor()
aList = []
bList = []
cur.execute('select wID from submissions where labNumber = 1 and url is not null')
data = cur.fetchall()
n = 0
cList = []
for x in data:
    a = str(x[0])
    aList.append(a)
q = True
while len(bList) < 10000:
    cList = random.sample(aList,3);
    if cList not in bList:
        bList.append(cList);
    cList = [];
print(len(data))
print (len(aList))       
print(bList)
print(len(bList))