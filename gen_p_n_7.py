#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CALCULO DE DIAGONALES: 7

#*******************
def prime_numbers(n):
    """
    Funcion que dado un numero devuelve una lista con los numeros primos hasta el dado
    
    Parametros:
    n  ->  integer
        """
    
    return ([2] + [x for x in range(3, n+1, 2) if not [y for y in range(3, int(x**0.5)+1, 2) if (float(x) / y).is_integer()]]) if n >= 2 else []
#**********************



l_prim = prime_numbers(1000)

for a in l_prim:
    p = 0
    n = 0
    npos = 0 
    ncont = 0
    
    while p < a:
        p +=2
        n = npos + 2
        
        while p > n:
            if  (2*n*a) + n**2 ==  (2*p*a) - p**2 :
                ncont += 1
                npos = n
                # print("a: {0:5d}  p:  {1:5d}   n: {2:5d}  b/c: {3:8d} ".format( int(a), p , n,  (2*n*a) + n**2 )  )
            
            n +=2

    print("{0:5d} {1:3d}".format(a,ncont))
