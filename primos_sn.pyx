#!/usr/bin/env python
# -*- coding: utf-8 -*-
def max_n_p(long a):

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
                ncont += 1
            
            n +=2

    print("{0:9d} {1:2d}".format(a,ncont))
