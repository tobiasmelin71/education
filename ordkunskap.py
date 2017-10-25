#!/usr/bin/env python
# -*- coding: utf-8 -*-
#run this program in a terminal with: python matteskola.py --level 1
#tested on Ubuntu 16.04

import argparse
import logging
import os
import random
import re
from random import randint

class WordTuple(object):
    def __init__(self, eng, swe):
        self.eng = eng
        self.swe = swe

    def getEng(self):
        return self.eng

    def getSwe(self):
        return self.swe

# Parse command line arguments
argparser = argparse.ArgumentParser(description="Ordkunskap engelska-svenska för Tova och Erik.")
argparser.add_argument("-l", "--level",
                        required = True,
                        dest = "level",
                        help = "Svårighetsgrad, har ingen effekt ännu")
args = argparser.parse_args()
level = eval(args.level)

print "Välkommen till Ordkunskap engelska-svenska\n\r"
def select():
    print "Välj vad du vill träna på:"
    print "\t Tryck 1 för svenska till engelska"
    print "\t Tryck 2 för engelska till svenska"  
    return (raw_input())

csvDelimiter = '\t'
words = []
with open("eng-swe-dictionary.txt") as f: #TODO remove all capital letters in that file
   for line in f:
      next = WordTuple(line.split(csvDelimiter)[0], 
                       line.split(csvDelimiter)[1][:-1]) # :-1 deletes last character (CR or LF?)
      words.append(next);
f.close()

while True:
    r = randint(0, len(words) - 1)
    print "\r\nVad betyder", words[r].getEng(), "?",
    svar = raw_input()
    if svar == words[r].getSwe(): # Must use == to compare the values
        print "Rätt"
    else:
        print "Fel. Rätt svar är", words[r].getSwe()










