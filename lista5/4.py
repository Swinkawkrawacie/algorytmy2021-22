#!/usr/bin/env python 

import turtle

def move_turtle(n, angle, step):
    """
    Move turtle to complete a step from a kochs curve

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
    if n==0:
        turtle.forward(step)
        return
    move_turtle(n-1, angle, step)
    turtle.left(angle)
    move_turtle(n-1, angle, step)
    turtle.right(180-angle)
    move_turtle(n-1, angle, step)
    turtle.left(angle)
    move_turtle(n-1, angle, step)

def koch_snowflake(rec_amount, line_color='black', size=300):
    """
    Draw a koch snoflake

    @param rec_amount: (int) level of recursion in a function
    @param line_color: (str) color of the snowflake (optional, default - black)
    @param size: (int) size of the base line (optional, default - 300)
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
    turtle.left(60)
    for i in range(3):
        move_turtle(rec_amount, 60, size/(3**rec_amount))
        turtle.right(120)
    turtle.right(60)
    turtle.done()
    

if __name__=='__main__':
    koch_snowflake(4, 'green')