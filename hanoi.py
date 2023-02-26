# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:24:20 2023

@authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt

Assumptions: 

- Base case/simplest case: moving one disk to destination rod/to_rod, i.e. a tower of one disk and only one move.

- Function requires three moves, two of which are recursive calls:
    
        1. move n - 1 from from_rod to aux_rod
        2. move n from from_rod to to_rod
        3. move n - 1 from aux_rod to to_rod.

"""

def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
    if n == 0: #no more disks
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) # 1st recursive call
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod) # Moving the disk from from_rod to to_rod
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)# 2nd recursive call: moving remaining disk from aux to to_rod using from_rod.


TowerOfHanoi(3, 'A', 'C', 'B')  

"""

"""