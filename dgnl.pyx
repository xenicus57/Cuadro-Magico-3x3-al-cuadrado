#!/usr/bin/env python
# -*- coding: utf-8 -*-

def n_dgnl(long a):

    cdef long p, n, npos, ncont
    p = 0
    n = 0
    npos = 0
    ncont = 0
    
    while a > p:
        p +=2
        n = npos + 2
    
        while p > n:
            if  (2*n*a) + n**2 ==  (2*p*a) - p**2 :
                npos = n
                # ncont += 1
                # print("{0:8f} {1:8d} {2:8f}  b ó c: {3:12d}  K: {4:12d}".format( (a**2 + (2*n*a) + n**2 )**0.5, a , (a**2 - (2*n*a) + n**2 )**0.5 ,  (2*n*a) + n**2 ,   3*(a**2) ) )
                print("a: {0:8d} p: {1:8d} n: {2:8d}  b ó c: {3:12d}  K: {4:12d}".format( a, p, n, (2*n*a) + n**2, 3*(a**2) ) )
            n +=2

    # print("{0:9d} {1:2d}".format(a,ncont))
