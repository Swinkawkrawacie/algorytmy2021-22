#!/usr/bin/env python 
def hanoi(n,A,B,C):
    """
    Move n discs from A to C using B

    @param n: (int) amount of discs
    @params A,B,C: names of the stacks
    """
    #--------------checking given data---------------------------------
    if not isinstance(n, int):
        raise TypeError('the amount of dics has to be an integer')
    if n<0:
        raise ValueError('the amount of discs has to be positive')
    #------------------------------------------------------------------
    if n>=1:
        hanoi(n-1,A,C,B)
        move(A,C)
        hanoi(n-1,B,A,C)

def move(move_from,move_to):
    """
    Print the move of a disc

    @param move_from: name of the stack to move from
    @param move_to: name of the stack to move to
    """
    print('move disc from',move_from,'to', move_to)

if __name__=='__main__':
    print('------------------------')
    hanoi(1,'A','B','C')
    print('------------------------')
    hanoi(2,'A','B','C')
    print('------------------------')
    hanoi(3,'A','B','C')
    print('------------------------')
    hanoi(4,'A','B','C')