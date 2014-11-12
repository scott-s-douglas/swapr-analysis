# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3 as lite
import numpy as np
import matplotlib.pyplot as plt
con = lite.connect('../AnonymousS2014Campus.sqlite')
cur = con.cursor()
cur.execute('''SELECT itemIndex, response FROM responses
                WHERE url IN (SELECT DISTINCT url FROM experts
                WHERE label = 'Practice 2') AND (itemIndex % 2) = 1 
                AND itemIndex < 11 AND response != ''
                AND labNumber = 2
                ORDER BY itemIndex''')
data = cur.fetchall()
fig = plt.figure(figsize = (15,3))
histogram1 = fig.add_subplot(1,5,1)
histogram1.set_title('Scores for item number 1')
histogram1.set_ylabel('Number of students')
histogram1.set_xlabel('Different ratings')
widthOfBar = 0.3
ratingsFor1 = []
ratingsFor3 = []
ratingsFor5 = []
ratingsFor7 = []
ratingsFor9 = []
for x in range(len(data)) :
    if(data[x][0] == 1):
        ratingsFor1.append(data[x][1])
    elif(data[x][0] == 3):
        ratingsFor3.append(data[x][1])
    elif(data[x][0] == 5):
        ratingsFor5.append(data[x][1])
    elif(data[x][0] == 7):
        ratingsFor7.append(data[x][1])
    else:
        ratingsFor9.append(data[x][1])
intList1=[]
intList3=[]
intList5=[]
intList7=[]
intList9=[]
for i in ratingsFor1:
    i=str(i)
    i=int(i)
    intList1.append(i)
for i in ratingsFor3:
    i=str(i)
    i=int(i)
    intList3.append(i)
for i in ratingsFor5:
    i=str(i)
    i=int(i)
    intList5.append(i)
for i in ratingsFor7:
    i=str(i)
    i=int(i)
    intList7.append(i)
for i in ratingsFor9:
    i=str(i)
    i=int(i)
    intList9.append(i)
numberOfZeros = 0
numberOfOnes = 0
numberOfTwos = 0
numberOfThrees = 0
numberOfFours = 0
for i in intList1:
    if i == 0:
        numberOfZeros = numberOfZeros + 1
    elif i == 1:
        numberOfOnes = numberOfOnes + 1
    elif i == 2:
        numberOfTwos = numberOfTwos + 1
    elif i == 3:
        numberOfThrees = numberOfThrees + 1
    else:
        numberOfFours = numberOfFours + 1
finalList1 = [numberOfZeros,numberOfOnes,numberOfTwos,numberOfThrees,numberOfFours]
for i in intList3:
    if i == 0:
        numberOfZeros = numberOfZeros + 1
    elif i == 1:
        numberOfOnes = numberOfOnes + 1
    elif i == 2:
        numberOfTwos = numberOfTwos + 1
    elif i == 3:
        numberOfThrees = numberOfThrees + 1
    else:
        numberOfFours = numberOfFours + 1
finalList3 = [numberOfZeros,numberOfOnes,numberOfTwos,numberOfThrees,numberOfFours]
for i in intList5:
    if i == 0:
        numberOfZeros = numberOfZeros + 1
    elif i == 1:
        numberOfOnes = numberOfOnes + 1
    elif i == 2:
        numberOfTwos = numberOfTwos + 1
    elif i == 3:
        numberOfThrees = numberOfThrees + 1
    else:
        numberOfFours = numberOfFours + 1
finalList5 = [numberOfZeros,numberOfOnes,numberOfTwos,numberOfThrees,numberOfFours]
for i in intList7:
    if i == 0:
        numberOfZeros = numberOfZeros + 1
    elif i == 1:
        numberOfOnes = numberOfOnes + 1
    elif i == 2:
        numberOfTwos = numberOfTwos + 1
    elif i == 3:
        numberOfThrees = numberOfThrees + 1
    else:
        numberOfFours = numberOfFours + 1
finalList7 = [numberOfZeros,numberOfOnes,numberOfTwos,numberOfThrees,numberOfFours]
for i in intList9:
    if i == 0:
        numberOfZeros = numberOfZeros + 1
    elif i == 1:
        numberOfOnes = numberOfOnes + 1
    elif i == 2:
        numberOfTwos = numberOfTwos + 1
    elif i == 3:
        numberOfThrees = numberOfThrees + 1
    else:
        numberOfFours = numberOfFours + 1
finalList9 = [numberOfZeros,numberOfOnes,numberOfTwos,numberOfThrees,numberOfFours]
ax = fig.add_subplot(111)
N = 5
width = 0.05
menStd =   [0,0,0,0,0]
ind = np.arange(N)
rects1 = ax.bar(ind, finalList, width,
                color='black',
                yerr=menStd,
                error_kw=dict(elinewidth=2,ecolor='red'))
print(finalList1)
print(finalList3)
print(finalList5)
print(finalList7)
print(finalList9)


