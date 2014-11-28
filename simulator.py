from __future__ import division, print_function
import sqlite3 as lite
from numpy import mean as mean
from itertools import groupby
from datetime import date, datetime

a = [{1:5,3:6,5:10,7:20,9:0},
    {1:5,3:9,5:19,7:19,9:17},
    {1:15,3:16,5:0,7:2,9:10}]

def swaprMean(*args):
    '''Takes any number of dictionaries of equal length containing key:value pairs and returns a list of the values' elementwise means paired with their keys.'''
    if len(args) == 1:
        return args[0]
    elif len(args) > 1:
        # check if each arg has the same keys
        try:
            keys0 = args[0].keys()
        except:
            print(args)
        for arg in args[1:]:
            if arg.keys() != keys0:
                raise Exception('Arguments do not have the same keys!')

        # take elementwise means
        means = {}
        for key in keys0:
            means.update({key:mean([arg[key] for arg in args])})
        return means

def simulator(f,db=lite.connect('AnonymousS2014Campus.sqlite')):
    '''Feeds the ratings of all students in the groups table of db into f() and records the result in the results table of db.'''
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS results (row INTEGER PRIMARY KEY NOT NULL, time timestamp, groupnum int, style text, itemIndex int, result number, UNIQUE (groupnum, style, itemIndex) ON CONFLICT ABORT)''')
    cur.execute('''SELECT g.groupnum, g.wID, r.itemIndex, k.score 
        FROM groups g, responses r, responseKeys k
        WHERE
            g.wID = r.wID
            AND r.itemIndex % 2 = 1
            AND r.itemIndex < 11
            AND r.labNumber = k.labNumber
            AND r.itemIndex = k.itemIndex
            AND r.response = k.response
        ORDER BY g.groupnum, g.wID, r.itemIndex
        ''')
    data = cur.fetchall()
    # Sort data into lists of ratings
    for groupnum, groupData in groupby(data, key= lambda x: x[0]):
        print(groupnum)
        scores = []
        for wID, wIDData in groupby(groupData, key= lambda x: x[1]):
            thisScores = {}
            for datum in wIDData:
                thisScores.update({datum[2]:datum[3]})
            scores.append(thisScores)
        means = f(*scores)
        print(means)
        for itemIndex in means.keys():
            cur.execute('''INSERT INTO results VALUES (NULL, CURRENT_TIMESTAMP, ?,  ?, ?, ?)''',[groupnum, f.__name__, itemIndex, means[itemIndex]])
    db.commit()

simulator(swaprMean)
# print(swaprMean(*a))