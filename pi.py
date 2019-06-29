#!/usr/bin/python

from decimal import *

import time

getcontext().prec = input("how many digits of pi? ")

def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)

def chudnovskyBig(n): #http://en.wikipedia.org/wiki/Chudnovsky_algorithm
    pi = Decimal(0)
    k = 0
    while k < n:
        itime = time.time()
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
        print "iteration ",k, "runtime ", (time.time() - itime)
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi

i = input("how many iterations? ")
starttime = time.time()
print "\t Chudnovsky calculation of Pi"
print "Iteration number ",i, " ", chudnovskyBig(i)
print"total time of run: ",  (time.time() - starttime)
