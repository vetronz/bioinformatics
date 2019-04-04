import re
from sys import *

word = argv[1]

p = re.compile('\\b' + word + '\\b')

with open('entamoeba.txt') as in_file:
    for line in in_file:
        m = p.search(line)
        if m:
            sline = p.split(line)
            count = 1
            for i in sline:
                print (count, ":", i)
                count += 1
