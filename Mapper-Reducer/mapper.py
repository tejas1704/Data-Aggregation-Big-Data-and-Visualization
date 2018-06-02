#!/usr/bin/python
"""mapper.py"""

import sys
import string
import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')
#nltk.download('punkt')

from nltk.tokenize import word_tokenize

value=int(1)
try:
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        words = [w.lower() for w in words]
        special = ['#','@','rt',":","''","'",",",".","http://","https://","said","would","new","also","could","many","may","like","even","little","weasel","stil","get","fix","cc"]
        single = list(string.ascii_lowercase)
        op = [word for word in words if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        op = [w for w in op if not w in stop_words]
        op = [w for w in op if not w in special]
        op = [w for w in op if not w in single]
        for word in op:
            print( "%s\t%d" % (word.lower(), value) )
except:
    import traceback
    traceback.print_exc()