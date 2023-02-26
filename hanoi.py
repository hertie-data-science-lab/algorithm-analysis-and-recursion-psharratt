# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:24:20 2023

@authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt

Assumptions: 

- Base case/simplest case: moving one disk from source rod (from_rod) to destination rod (to_rod), i.e. a tower of one disk requiring only one move.

- To move n disks, function requires three steps, two of which are recursive calls:
    
        1. move n - 1 from from_rod to aux_rod
        2. move n from from_rod to to_rod
        3. move n - 1 from aux_rod to to_rod.
        
Notes: 

- The function has 2^n-1 time complexity. We tested this with the move counter.

"""
# Move counter init for tracking complexity
MoveCount = 0 

def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
    # Base case
    if n == 0: 
        return
    # Counter for moves
    global MoveCount
    MoveCount += 1 
    # 1st recursive call: moving the n-1 disk from from_rod to aux using to_rod
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    # Moving the disk from from_rod to to_rod
    print("Disk", n, "moves from rod", from_rod, "to rod", to_rod) 
    # 2nd recursive call: moving disk from aux to to_rod using from_rod.
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


TowerOfHanoi(3, 'A', 'C', 'B')  

print("Total moves:", MoveCount)
