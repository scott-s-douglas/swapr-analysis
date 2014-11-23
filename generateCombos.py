import sqlite3 as lite
import random

con = lite.connect('AnonymousS2014Campus.sqlite')
cur = con.cursor()
aList = []
bList = []
cur.execute('''select wID from submissions
                WHERE labNumber = 1 AND url is not null''')

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
    
cur.execute('''CREATE TABLE IF NOT EXISTS groups (groupnum int, wID text)''')
groupnum = 0
for x in bList:
    count = 0
    while count < len(x):
        wid = str(x[count])
        # print(groupnum, wid)
        cur.execute('''INSERT INTO groups VALUES(?, ?)''', [groupnum, wid])
        count = count + 1
    groupnum = groupnum + 1
    

print(len(data))
print (len(aList))       
# print(bList)
print(len(bList))

con.commit()
