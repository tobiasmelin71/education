#!/usr/bin/env python
# -*- coding: utf-8 -*-
#to know how to use this program do: python filename --help
#tested on Ubuntu 16.04

import argparse
import logging
import os
import random
import time
from random import randint

class Tuple(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

def numInput():
    while True:
        try:
            number = int(input())
            return number
            break
        except:
            print "Du måste svara med ett tal"

# Parse command line arguments
argparser = argparse.ArgumentParser(description="Öva division.")
argparser.add_argument("--start",
                        required = True,
                        dest = "start",
                        help = "minsta nämnare & kvot")
argparser.add_argument("--stop",
                        required = True,
                        dest = "stop",
                        help = "högsta nämnare & kvot")
args = argparser.parse_args()
start = eval(args.start)
stop = eval(args.stop)

problems = []
nOfProblems = 0
for i in range(start, stop + 1):
    for j in range(start, stop + 1):
        next = Tuple (i, j)
        problems.append(next)
        nOfProblems = nOfProblems + 1

random.seed()
nOfCorrectAnswers = 0
nOfAnswers = 0
startTime = time.time()

while nOfProblems > 0:
    r = randint(0, nOfProblems - 1)
    namnare = int(problems[r].getX())
    kvot = int(problems[r].getY())
    taljare = kvot * namnare
    correctAnswer = kvot
    print taljare, "/", namnare, "=",

    usersAnswer = numInput()
    nOfAnswers = nOfAnswers + 1
    if usersAnswer == correctAnswer:
        nOfCorrectAnswers = nOfCorrectAnswers + 1;
        print "Rätt. Du har svarat rätt", nOfCorrectAnswers,  "av", nOfAnswers, "gånger på", int(time.time() - startTime), "sekunder"
    else:
        print "Fel. Rätt svar är", correctAnswer

    problems.pop(r)
    nOfProblems = nOfProblems - 1

assert nOfProblems == 0, "FATAL: nOfProblems still not zero"
