#!/usr/bin/python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    
    line = line.strip()
    
    #word, count = line.split('\t')
    data_map=line.split('\t')
    word,count=data_map
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print( "%s\t%d" % (current_word, current_count) )
        current_count = count
        current_word = word

if current_word == word:
    print( "%s\t%d" % (current_word, current_count) )