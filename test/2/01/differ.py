#!/usr/bin/env python
import difflib
import sys

try:
    text_file1 = sys.argv[1]
    text_file2 = sys.argv[2]
except Exception , e:
    print "Error: "+str(e)
    print "Usage: differ.py file1_name file2_name"
    sys.exit()

def read_file(filename):
    try:
        file_open = open(filename , 'rb')
        text = file_open.read().splitlines()
        file_open.close()
        return text
    except IOError as error :
        print 'Read file Error :'+str(error)
        sys.exit()
if text_file1 == "" or text_file2 == "":
    print 'USage: differ.py file1_name file2_name'
    sys.exit()
text1_lines = read_file(text_file1)
text2_lines = read_file(text_file2)

d = difflib.HtmlDiff()
print d.make_file(text1_lines , text2_lines)

