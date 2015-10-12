#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python implementation of Huffman Coding

This program implements the huffman coding used for encoding a group of symbols
by a preface
"""
__author__ =  'Ismael Taboada'
__version__=  '1.0'


from collections import defaultdict
import csv
import os.path
import time
from huffmantree import HuffmanCoding

DEBUG = False
DIA_FILE = 'huffman.tree'
LOG_FILE = 'log.csv'
TEST = "this is an example for huffman encoding"

try:
    pass
except Exception as e:
    print "\nGraphviz software not found.\nPlease install Graphviz software on your computer.(http://www.graphviz.org/Download.php)"
    exit(1)


txtin = raw_input("Write some symbols(blank for sample case):")
txtin = TEST if txtin=="" else txtin
txtout = txtin
symb2freq = defaultdict(int)
for ch in txtin:
    if ch == "":
        ch = "SPACE"
    symb2freq[ch] += 1

start = time.time()
huff = HuffmanCoding()
huff.encode(symb2freq)
end = time.time()
time_lapse = end - start
coding_table = huff.tree_to_table()

print "Codes table"
print "Symbol\tFrec\tCode"
for coding in coding_table:
    print "\t".join(map(str,coding))
    # Replace at the input text the symbol with the propper code
    txtout = txtout.replace(coding[0],coding[2])
print "Time: ",time_lapse,"ms"

print "\nText input:",txtin
print "Text output:",txtout

dot = huff.tree_to_graph()
print "\nDiagram saved at: ",DIA_FILE+'.png'
dot.render(DIA_FILE, view=DEBUG)
dot.render('graph.png')

log_exits = os.path.isfile(LOG_FILE)

with open(LOG_FILE, 'ab') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    if not log_exits:
        spamwriter.writerow(['length', 'time'])
    spamwriter.writerow([len(txtin), time_lapse])

print 'Log update at: ',LOG_FILE
