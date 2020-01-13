#!/usr/bin/env python
# -*- coding: utf-8 -*-

import primos_sn

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

for i in l_prim:
    primos_sn.max_n_p(i) 
