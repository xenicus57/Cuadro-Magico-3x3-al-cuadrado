#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CALCULO DE DIAGONALES: 2


# *******************************
def entero(x):
    """
    Función que nos indica si un numero puede considerarse entero
    Parametros:
    x -> cualquier número

    NOTA: Vamos a suponer que no nos encontraremos con una comparación de este estilo :
    2.9999999999999 == 3.0  
    porque python devolveria verdadero
    """

    if x-int(x) == 0:
        return True
    else:
        return False

# ******************

p = 2
n = 0
ncont = 0

while True:
    p +=2
    n = 2
    while p > n:
               
        a = (p**2 + n**2) / (2*(p-n))
        if entero( a ):
            ncont += 1
            print("a: {0:5d}  p:  {1:5d}   n: {2:5d}".format( int(a), p , n ) )
           

        n +=2
    
    # Nuestro punto de rotura
    if ncont > 500:
        break

