#!/usr/bin/env python
# -*- coding: utf-8 -*-
#run this program in a terminal with: python matteskola.py --level 1
#tested on Ubuntu 16.04

import argparse
import logging
import os
import random
import re
import sys
import time
from random import randint

class status(object):
    def __init__(self):
        self.nofCorrect = 0
        self.nofFail = 0

    def incrementNofCorrect(self):
        self.nofCorrect += 1

    def incrementNofFail(self):
        self.nofFail += 1

    def getNofCorrect(self):
        return self.nofCorrect

    def getNofFail(self):
        return self.nofFail

    def getTotal(self):
        return (self.nofCorrect + self.nofFail)

def numInput():
    while True:
        try:
            number = int(input())
            return number
            break
        except:
            print "Du måste svara med ett tal"

def select():
    print "Välj vad du vill träna på:"
    print "\t Tryck a för addition"
    print "\t Tryck s för subtraktion"
    print "\t Tryck m för multiplikation"
    print "\t Tryck d för division"
    print "\t Tryck b för blandat med alla räknesätten"   
    return (raw_input())

def addition():
    a = randint(0, 10*level)
    b = randint(0, 10*level)
    print "\r\n", a, "+", b,"=",
    svar = numInput()
    if (a + b) == svar:
        myStatus.incrementNofCorrect()
        print "Rätt. Du har svarat rätt", myStatus.getNofCorrect(),  "av", myStatus.getTotal(), "gånger på",
    else:
        myStatus.incrementNofFail()
        print "Fel. Rätt svar är", a + b
    return svar

def subtraktion():
    a = randint(0, 10*level)
    b = randint(0, 10*level)
    if a < b:
        c = b
        b = a
        a = c
    print "\r\n", a, "-", b,"=",
    svar = numInput()
    if (a - b) == svar:
        myStatus.incrementNofCorrect()
        print "Rätt. Du har svarat rätt", myStatus.getNofCorrect(),  "av", myStatus.getTotal(), "gånger på",
    else:
        myStatus.incrementNofFail()
        print "Fel. Rätt svar är", a - b
    return svar

def multiplikation():
    a = randint(2, 3*level)
    b = randint(2, 3*level)
    print "\r\n", a, "*", b,"=",
    svar = numInput()
    if (a * b) == svar:
        myStatus.incrementNofCorrect()
        print "Rätt. Du har svarat rätt", myStatus.getNofCorrect(),  "av", myStatus.getTotal(), "gånger på",
    else:
        myStatus.incrementNofFail()
        print "Fel. Rätt svar är", a * b
    return svar

def division():
    a = randint(1, 3*level)
    b = randint(0, 3*level)  
    print "\r\n", a * b, "/", a, "=",
    svar = numInput()
    if (b) == svar:
        myStatus.incrementNofCorrect()
        print "Rätt. Du har svarat rätt", myStatus.getNofCorrect(),  "av", myStatus.getTotal(), "gånger på",
    else:
        myStatus.incrementNofFail()
        print "Fel. Rätt svar är", b
    return svar

# Parse command line arguments
argparser = argparse.ArgumentParser(description="Matteskola för Tova och Erik.")
argparser.add_argument("-l", "--level",
                        required = True,
                        dest = "level",
                        help = "Svårighetsgrad (1 = lättast, ju högre desto svårare)")
args = argparser.parse_args()

level = eval(args.level)
print "Välkommen till Eriks och Tovas matteskola\n\r"
random.seed()
myStatus = status()
raknesatt = select()
startTime = time.time()

while True:
    valtRaknesatt = raknesatt
    if raknesatt is "b":
        listaMedRaknesatt = ["a", "s", "m", "d"]
        slumptal = randint(0, 3)
        valtRaknesatt = listaMedRaknesatt[slumptal]
    if valtRaknesatt is "a":
        retValue = addition()
    if valtRaknesatt is "s":
        retValue = subtraktion()
    if valtRaknesatt is "m":
        retValue = multiplikation()
    if valtRaknesatt is "d":
        retValue = division()
    if retValue == -1:
        break
    currentTime = time.time()
    print int(currentTime - startTime), "sekunder"

sys.exit(0)

