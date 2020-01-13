#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CALCULO DE DIAGONALES: 1


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

# Dos variables para definir desde donde hasta donde quiero los cálculos.
ini = 1
fin = 301

for i in range(ini, fin):
    a = i**2
    bini = 1
    bfin = a
    for b in range(bini,bfin):
        if entero((a+b)**0.5 ) and entero((a-b)**0.5 ) :
            # ojo el formato esta calculado segun el valor que he colocado a la variable fin
            print("{0:4d} {1:4d} {2:4d}".format( int((a+b)**0.5) , i , int((a-b)**0.5)),"b:", b ,"K:",int(3*a) )


