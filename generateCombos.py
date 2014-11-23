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
#for j in bList
#    wid1 = str(x[0])
#    cur.execute('''INSERT INTO groups
#                    VALUES(?,?)''',
#                    [bList.index,wid1]);

print(len(data))
print (len(aList))       
print(bList)
print(len(bList))


