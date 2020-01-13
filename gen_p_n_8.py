#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CALCULO DE DIAGONALES: 8

import primos_sn


l_prim = [ 3, 3**2, 3**3, 3**4, 3**5,
           7, 7**2, 7**3, 7**4, 7**5, 
           11, 11**2, 11**3, 11**4, 11**5,
           19, 19**2, 19**3, 19**4, 
           23, 23**2, 23**3, 23**4, ] 


for i in l_prim:
   primos_sn.max_n_p(i) 
