#!/usr/bin/python
"""reducer.py"""

from operator import itemgetter
import sys

top10words = ['facebook',
 'zuckerberg',
 'mark',
 'disgusting',
 'greedy',
 'fb',
 'still',
 'million',
 'sign',
 'open']

current_word = None
current_count = 0
word = None
topten = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

for line in sys.stdin:
    
    line = line.strip()
    
    data_map=line.split('\t')
    word,count=data_map
    try:
        count = int(count)
    except ValueError:
        continue
    
    for i in range(len(top10words)):
        count = 0
        if top10words[i] == word.lower():
            topten[i] += 1
print(topten)

for i in range(len(top10words)):
    for j in range(1,len(top10words)):
        if i != j:
            print(top10words[i]+ '-' +top10words[j] + ' ' + str(min(topten.get(i), topten.get(j))))