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

class binom:
    """
    The representation of the probability for specific parameters
    """
    def __init__(self, n, k, p, all_list=[], mult=0):
        #---------checking-given-data----------------------------------
        if not isinstance(n, int) or not isinstance(k, int) or not(isinstance(p, int) or isinstance(p,float)) or not isinstance(all_list,list) or not isinstance(mult, int):
            raise TypeError('incorrect type of given data')
        if k<0 or n<0:
            raise ValueError('arguments should be positive')
        if p<0 or p>1:
            raise ValueError('probability of success should be a number between 0 and 1')
        #--------------------------------------------------------------
        self.n = n
        self.k = k
        self.p = p
        self.all_list = all_list
        self.mult = mult
        self.calc_value()
        self.value = self.all_list[self.k-1]
        self.s = sum(self.all_list[i] for i in range(self.k+1))
        
    def calc_value(self, mult_in=0):
        """
        Calculate the value of the specific probability also keep record of all of the parts of the sum

        @param mult_in: (int) variable for counting multiplications (optional)
        @return (list) the value of the probability and the amount of multiplications in a form of a list
        """        
        if self.k>self.n:
            return [0, mult_in]
        if self.k==self.n or self.k==0:
            power = new_power((1-self.p),self.n)
            mult_in += power[1]
            if len(self.all_list)==0 or len(self.all_list)==self.k:
                self.all_list.append(power[0])
            return [power[0], mult_in]
        mult_in += 4
        x = binom(self.n,self.k-1,self.p,self.all_list).calc_value(mult_in)
        result = x[0]*self.p*(self.n-self.k+1)/((1-self.p)*self.k)
        mult_in = x[1]
        if len(self.all_list)==self.k:
            self.all_list.append(result)
        self.mult = mult_in
        return [result, mult_in]

def probability(n, k, p):
    #---------checking-given-data----------------------------------
    if k<0 or n<0:
        raise ValueError('arguments should be positive')
    if p<0 or p>1:
        raise ValueError('probability of success should be a number between 0 and 1')
    #--------------------------------------------------------------
    if n == 0:
        return(0,0)
    elif n==k:
        return (1,0)
    else:
        new_prob = binom(n,k,p)
        prob = new_prob.s
        count_mult = new_prob.mult
        return (prob,count_mult)
