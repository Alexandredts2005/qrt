# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:26:08 2021

@author: lvannier
"""

from time import time

start=time()

def dichotomie(tab, v):
    k=0 #compteur d'opérations
    a = 0
    b = len(tab) - 1
    while a <= b:
        m = (a + b) // 2
        k=k+1
        if tab[m] == v:  # on trouve v
            return True,k
        elif tab[m] < v:
            a = m + 1
            k=k+1
        else:
            b = m - 1
            k=k+1
    # on ne trouve pas v et a > b
    return False,k

n=100000
L = [i for i in range(n)]



print(dichotomie(L, n))


end=time()
print(end-start)