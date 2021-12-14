#!/usr/bin/env python 

import turtle

def turtle_move(n, angle, step):
    """
    Move turtle to complete a step from the hilberts curve

    @param n: (int) level of recursion in a function
    @param angle: (int) angle to turn the turtle
    @param step: (int/float) length of one part of the curve
    """
    #----------------checking given data-------------------
    if not (isinstance(n, int) and isinstance(angle, int) and (isinstance(step, int) or isinstance(step, float))):
        raise TypeError('data need to be integers (step can be also a float)')
    if n<0:
        raise ValueError('level of the recursion cannot be negative')
    #------------------------------------------------------
    if n == 0:
        return
    turtle.left(angle)
    turtle_move(n-1, -angle, step)
    turtle.forward(step)
    turtle.right(angle)
    turtle_move(n-1, angle, step)
    turtle.forward(step)
    turtle_move(n-1, angle, step)
    turtle.right(angle)
    turtle.forward(step)
    turtle_move(n-1, -angle, step)
    turtle.left(angle)

def hilbert_curve(rec_amount, line_color='black', size=300):
    """
    Draw a hilberts curve

    @param rec_amount: (int) level of recursion in a function
    @param line_color: (str) color of the curve (optional, default - black)
    @param size: (int) size of the square to fill (optional, default - 300)
    """
    #--------------checking given data------------------------
    if not (isinstance(rec_amount,int) and isinstance(line_color,str) and isinstance(size, int)):
        raise TypeError('incorrect type of given data')
    if size<=0:
        raise ValueError('size is too small')
    #---------------------------------------------------------
    turtle.penup()
    turtle.goto(-size/2,-size/2)
    turtle.pendown()
    try:
        turtle.color(line_color)
    except:
        raise ValueError('given color is incorrect')
    turtle_move(rec_amount, 90, size/(2**rec_amount-1))
    turtle.done()

if __name__=='__main__':
    hilbert_curve(3)