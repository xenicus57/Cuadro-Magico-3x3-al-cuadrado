#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CALCULO DE DIAGONALES: 5

lista = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024] 

for a in lista:
    p = 0
    n = 0
    npos = 0 
    
    while p < a:
        p +=2
        n = npos + 2
        
        while p > n:
            if  (2*n*a) + n**2 ==  (2*p*a) - p**2 :
                npos = n
                print("a: {0:5d}  p:  {1:5d}   n: {2:5d}  b/c: {3:8d} ".format( int(a), p , n,  (2*n*a) + n**2 )  )
              
            n +=2

