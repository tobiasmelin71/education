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

class Tuple(object):
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital

    def getCountry(self):
        return self.country

    def getCapital(self):
        return self.capital

# Parse command line arguments
argparser = argparse.ArgumentParser(description="Geografi för Tova och Erik.")
argparser.add_argument("-l", "--level",
                        required = True,
                        dest = "level",
                        help = "Svårighetsgrad, har ingen effekt ännu")
args = argparser.parse_args()
level = eval(args.level)

print "Välkommen till Geografi Europa\n\r"
def select():
    print "Välj vad du vill träna på:"
    print "\t Tryck 1 för svenska till engelska"
    print "\t Tryck 2 för engelska till svenska"  
    return (raw_input())

csvDelimiter = ', '
pairs = []
with open("contries-capitals.txt") as f:
   for line in f:
      next = Tuple(line.split(csvDelimiter)[0], 
                       line.split(csvDelimiter)[1][:-1]) # :-1 deletes last character (CR or LF?)
      pairs.append(next);
f.close()

while True:
    a = randint(0, 1)
    if a == 0:
        r = randint(0, len(pairs) - 1)
        print "\r\nVad heter huvudstaden i", pairs[r].getCountry(), "?",
        svar = raw_input()
        if svar == pairs[r].getCapital(): # Must use == to compare the values
            print "Rätt"
        else:
            print "Fel. Rätt svar är", pairs[r].getCapital()
    else:
        r = randint(0, len(pairs) - 1)
        print "\r\nI vilket land är", pairs[r].getCapital(), "huvudstad ?",
        svar = raw_input()
        if svar == pairs[r].getCountry(): # Must use == to compare the values
            print "Rätt"
        else:
            print "Fel. Rätt svar är", pairs[r].getCountry()









