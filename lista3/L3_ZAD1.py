#!/usr/bin/env python

def new_power(base,power,k=0):
    """
    Calculate power from given data

    @param base: (int/float) base of the exponentation
    @param power: (int) power of the exponentation
    return: (list) result of the exponentation and the amount of multiplication needed to complete the task in a form of a list
    """
    #---------checking-given-data----------------------------------
    if not(isinstance(base, int) or isinstance(base, float)) or not isinstance(power, int):
        raise TypeError('incorrect type of given data')
    #--------------------------------------------------------------
    if power==0:
        return [1,k]
    if power%2 == 0:
        k += 2
        return new_power(base*base,power//2,k)
    else:
        k += 3
        new = new_power(base*base,power//2,k)
        return [new[0]*base,new[1]]

def binom(n,k):
    """
    Calculate binomial without multiplications
    """
    if k>n:
        return 0
    if k==0 or n==k:
        return 1
    return binom(n-1,k-1)+binom(n-1,k)

def probability(n, k, p):
    
    if k>n or k<0 or n<=0:
        raise ValueError('given data is incorrect')
    
    count_mult = 0
    all_sum = 1
    base1 = new_power(1-p, n)
    base = base1[0]
    if k>0:
        mult1 = p/(1-p)
        mult2 = p/(1-p)
        count_mult += 2+base1[1]
        all_sum += binom(n,1)*mult2
        count_mult += 1
        if k>1:
            for i in range(2, k+1):
                mult2 *= mult1
                all_sum += binom(n,i)*mult2
                count_mult += 2
    else:
        prob = base
        return (prob,count_mult)


    prob = all_sum*base
    count_mult += 1
    return (prob,count_mult)

if __name__ == '__main__':
    
    print(probability(20,3,0.2))
    print(probability(20,20,0.2))
    print(probability(20,1,0.2))
    print(probability(20,19,0.2))
    print(probability(5,0,0.2))
    print(probability(0,0,0.2))
    print(new_power(0.8,5))
    