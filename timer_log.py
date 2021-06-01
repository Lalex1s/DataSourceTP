# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:20:41 2021

@author: lalex
"""

import time
from collections import Counter


def timeit(method):
    def timed(*args,**kwargs):
        ts = time.time()
        result = method(*args,**kwargs)
        te = time.time()
        print(te-ts)
        return result
    return timed

@timeit
def CountWordDict(textfile):
    text = open(textfile, "r")
    d = dict()
    
    for line in text:
    	line = line.strip()
    	line = line.lower()
    	words = line.split(" ")
    
    	for word in words:
    		if word in d:
    			d[word] = d[word] + 1
    		else:
    			d[word] = 1
    # Print the contents of dictionary
    for key in list(d.keys()):
     	print(key, ":", d[key])


@timeit
def CountWordCounter(textfile):
    text = open(textfile, "r")
    d = dict()
    words = []
    for line in text:
    	line = line.strip()
    	line = line.lower()
    	words += line.split(" ")
    d = Counter(words)
    for key in list(d.keys()):
     	print(key, ":", d[key])


 
CountWordDict("t8.shakespeare.txt")
time.sleep(10)
CountWordCounter("t8.shakespeare.txt")





