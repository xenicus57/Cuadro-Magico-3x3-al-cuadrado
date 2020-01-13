#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CALCULO DE DIAGONALES: 3



for a in range(1,81):
    p = 0
    n = 0

    while p < (2 * a):
        p +=2
        n = 2
        while p > n:
        
            if  (2*n*a) + n**2 ==  (2*p*a) - p**2 :
                print("a: {0:5d}  p:  {1:5d}   n: {2:5d}  b/c: {3:8d} ".format( int(a), p , n,  (2*n*a) + n**2 )  )
            
            n +=2

