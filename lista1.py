#!/usr/bin/env python

def find_lcm(first:int, second:int):
    """
    Find the least common multiple of two positive integers

    @param first: (int) first number
    @param second: (int) second number
    @return: (int) the least common multiple
    """
    #---------checking-given-data----------------------------------
    if not isinstance(first, int) or not isinstance(second, int):
        raise TypeError('numbers for the lcm should be integers')
    if first <= 0 or second <= 0:
        raise ValueError('numbers for the lcm should be positive')
    #--------------------------------------------------------------
    n=1
    if first > second:
        bigger = first
        smaller = second
    elif first == second:
        return first
    else:
        bigger = second
        smaller = first

    while (bigger*n)%smaller != 0:
        n += 1
    return bigger*n

def find_gcf(first:int, second:int):
    """
    Find the greatest common factor of two positive integers

    @param first: (int) first number
    @param second: (int) second number
    @return: (int) the greatest common factor
    """
    #---------checking-given-data----------------------------------
    if not isinstance(first, int) or not isinstance(second, int):
        raise TypeError('numbers for the gcf should be integers')
    #--------------------------------------------------------------
    if abs(first) > abs(second):
        bigger = first
        smaller = second
    elif abs(first) == abs(second):
        return first
    else:
        bigger = second
        smaller = first

    max = 1
    for i in range(1, smaller+1):
        if smaller%i == 0 and bigger%i == 0:
            max = i
    return max

class Fraction:
    """
    Representation of a fraction
    """
    def __init__(self, numerator:int, denominator:int):
        #---------checking-given-data----------------------------------
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError('numbers for the fraction should be integers')
        if denominator == 0:
            raise ValueError('division by zero')
        #--------------------------------------------------------------
        if denominator < 0:
            numerator *= -1
            denominator *= -1

        common = find_gcf(denominator, numerator)
        self.numerator = int(numerator/common)
        self.denominator = int(denominator/common)
    
    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other):
        #---------checking-given-data----------------------------------
        if not isinstance(other, Fraction):
            raise TypeError('adding not a fraction')
        #--------------------------------------------------------------
        if self.denominator == other.denominator:
            return Fraction(self.numerator+other.numerator,self.denominator)
        else:
            common = find_lcm(self.denominator, other.denominator)
            first_mul = common/self.denominator
            second_mul = common/other.denominator
            return Fraction(int(first_mul*self.numerator+second_mul*other.numerator), common)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        #---------checking-given-data----------------------------------
        if not isinstance(other, Fraction):
            raise TypeError('subtracting not a fraction')
        #--------------------------------------------------------------
        if self.denominator == other.denominator:
            return Fraction(self.numerator-other.numerator,self.denominator)
        else:
            common = find_lcm(self.denominator, other.denominator)
            first_mul = common/self.denominator
            second_mul = common/other.denominator
            return Fraction(int(first_mul*self.numerator-second_mul*other.numerator), common)

    def __rsub__(self, other):
        new = self - other
        return Fraction((-1)*new.numerator, new.denominator)

    def __mul__(self, other):
        #---------checking-given-data----------------------------------
        if not isinstance(other, Fraction):
            raise TypeError('multiplying by not a fraction')
        #--------------------------------------------------------------
        return Fraction(int(self.numerator*other.numerator), int(self.denominator*other.denominator))
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        #---------checking-given-data----------------------------------
        if not isinstance(other, Fraction):
            raise TypeError('dividing by not a fraction')
        #--------------------------------------------------------------
        return Fraction(int(self.numerator*other.denominator), int(self.denominator*other.numerator))

    def __rtruediv__(self, other):
        return Fraction(int(other.numerator*self.denominator), int(other.denominator*self.numerator))

    def getNum(self):
        """
        Get the numerator of a specific fraction
        """
        return self.numerator

    def getDem(self):
        """
        Get the denominator of a specific fraction
        """
        return self.denominator
    
    def __eq__(self, other):
        #---------checking-given-data----------------------------------
        if not isinstance(other, Fraction):
            raise TypeError('comparing with not a fraction')
        #--------------------------------------------------------------
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False
    
    def __ne__(self, other):
        #---------checking-given-data----------------------------------
        if not isinstance(other, Fraction):
            raise TypeError('comparing with not a fraction')
        #--------------------------------------------------------------
        return not(self==other)

    def __gt__(self, other):
        #---------checking-given-data----------------------------------
        if not isinstance(other, Fraction):
            raise TypeError('comparing with not a fraction')
        #--------------------------------------------------------------
        common = find_lcm(self.denominator, other.denominator)
        first_mul = common/self.denominator
        second_mul = common/other.denominator
        if self.numerator*first_mul > other.numerator*second_mul:
            return True
        else:
            return False
    
    def __lt__(self, other):
        #---------checking-given-data----------------------------------
        if not isinstance(other, Fraction):
            raise TypeError('comparing with not a fraction')
        #--------------------------------------------------------------
        common = find_lcm(self.denominator, other.denominator)
        first_mul = common/self.denominator
        second_mul = common/other.denominator
        if self.numerator*first_mul < other.numerator*second_mul:
            return True
        else:
            return False
    
    def __ge__(self, other):
        #---------checking-given-data----------------------------------
        if not isinstance(other, Fraction):
            raise TypeError('comparing with not a fraction')
        #--------------------------------------------------------------
        common = find_lcm(self.denominator, other.denominator)
        first_mul = common/self.denominator
        second_mul = common/other.denominator
        if self.numerator*first_mul >= other.numerator*second_mul:
            return True
        else:
            return False
    
    def __le__(self, other):
        #---------checking-given-data----------------------------------
        if not isinstance(other, Fraction):
            raise TypeError('comparing with not a fraction')
        #--------------------------------------------------------------
        common = find_lcm(self.denominator, other.denominator)
        first_mul = common/self.denominator
        second_mul = common/other.denominator
        if self.numerator*first_mul <= other.numerator*second_mul:
            return True
        else:
            return False

class FractionExtended(Fraction):
    """
    Representation of a fraction
    """
    def __init__(self, numerator, denominator):
        #---------checking-given-data----------------------------------
        if not (isinstance(numerator, int) or isinstance(numerator, float)) or not (isinstance(denominator, int) or isinstance(denominator, float)):
            raise TypeError('numbers for the fraction should be integers or floats')
        if denominator == 0:
            raise ValueError('division by 0')
        #--------------------------------------------------------------
        if denominator < 0:
            numerator *= -1
            denominator *= -1
        if denominator == 0:
            raise ValueError
        if isinstance(numerator, float):
            numerator = round(numerator,5)
            while numerator%1 != 0:
                numerator *= 10
                denominator *= 10
        if isinstance(denominator, float):
            denominator = round(denominator,5)
            while denominator%1 != 0:
                numerator *= 10
                denominator *= 10

        denominator = int(denominator)
        numerator = int(numerator)
        common = find_gcf(denominator, numerator)
        self.numerator = int(numerator/common)
        self.denominator = int(denominator/common)

    def __add__(self, other):
        if isinstance(other, Fraction) or isinstance(other, FractionExtended):
            sum1 = Fraction(self.numerator, self.denominator)+Fraction(other.numerator, other.denominator)
            return FractionExtended(sum1.numerator, sum1.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            new_other = FractionExtended(other, 1)
            sum1 = Fraction(self.numerator, self.denominator)+Fraction(new_other.numerator, new_other.denominator)
            return FractionExtended(sum1.numerator, sum1.denominator)
        else:
            raise TypeError('adding not a number')

    def __sub__(self, other):
        if isinstance(other, Fraction) or isinstance(other, FractionExtended):
            sub1 = Fraction(self.numerator, self.denominator)-Fraction(other.numerator, other.denominator)
            return FractionExtended(sub1.numerator, sub1.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            new_other = FractionExtended(other, 1)
            sub1 = Fraction(self.numerator, self.denominator)-Fraction(new_other.numerator, new_other.denominator)
            return FractionExtended(sub1.numerator, sub1.denominator)
        else:
            raise TypeError('subtracting not a number')
    
    def __mul__(self, other):
        if isinstance(other, Fraction) or isinstance(other, FractionExtended):
            mul1 = Fraction(self.numerator, self.denominator)*Fraction(other.numerator, other.denominator)
            return FractionExtended(mul1.numerator, mul1.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            new_other = FractionExtended(other, 1)
            mul1 = Fraction(self.numerator, self.denominator)*Fraction(new_other.numerator, new_other.denominator)
            return FractionExtended(mul1.numerator, mul1.denominator)
        else:
            raise TypeError('multiplying by not a number')

    def __truediv__(self, other):
        if isinstance(other, Fraction) or isinstance(other, FractionExtended):
            div1 = Fraction(self.numerator, self.denominator)/Fraction(other.numerator, other.denominator)
            return FractionExtended(div1.numerator, div1.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            new_other = FractionExtended(other, 1)
            div1 = Fraction(self.numerator, self.denominator)/Fraction(new_other.numerator, new_other.denominator)
            return FractionExtended(div1.numerator, div1.denominator)
        else:
            raise TypeError('dividing by not a number')

    def mixed(self, switch):
        """
        Find a mixed form of the given fracture

        @param switch: (bool) information if the fraction shoould be returned in a mixed form
        @return: (str) representation of a fractor in a wanted form
        """
        #---------checking-given-data----------------------------------
        if not isinstance(switch, bool):
            raise TypeError('switch can only')
        #--------------------------------------------------------------
        if switch == True:
            first = int(self.numerator//self.denominator)
            second = self.numerator%self.denominator
            return str(first)+';'+str(FractionExtended(second, self.denominator))
        else:
            return self.__str__()
    
    def __eq__(self, other):
        if isinstance(other, Fraction) or isinstance(other, FractionExtended):
            return Fraction(self.numerator, self.denominator) == Fraction(other.numerator, other.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            new_other = FractionExtended(other, 1)
            return Fraction(self.numerator, self.denominator) == Fraction(new_other.numerator, new_other.denominator)
        else:
            raise TypeError('comparing with not a number')
    
    def __ne__(self, other):
        if isinstance(other, Fraction) or isinstance(other, FractionExtended):
            return Fraction(self.numerator, self.denominator) != Fraction(other.numerator, other.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            new_other = FractionExtended(other, 1)
            return Fraction(self.numerator, self.denominator) != Fraction(new_other.numerator, new_other.denominator)
        else:
            raise TypeError('comparing with not a number')

    def __gt__(self, other):
        if isinstance(other, Fraction) or isinstance(other, FractionExtended):
            return Fraction(self.numerator, self.denominator) > Fraction(other.numerator, other.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            new_other = FractionExtended(other, 1)
            return Fraction(self.numerator, self.denominator) > Fraction(new_other.numerator, new_other.denominator)
        else:
            raise TypeError('comparing with not a number')
    
    def __lt__(self, other):
        if isinstance(other, Fraction) or isinstance(other, FractionExtended):
            return Fraction(self.numerator, self.denominator) < Fraction(other.numerator, other.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            new_other = FractionExtended(other, 1)
            return Fraction(self.numerator, self.denominator) < Fraction(new_other.numerator, new_other.denominator)
        else:
            raise TypeError('comparing with not a number')
    
    def __ge__(self, other):
        if isinstance(other, Fraction) or isinstance(other, FractionExtended):
            return Fraction(self.numerator, self.denominator) >= Fraction(other.numerator, other.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            new_other = FractionExtended(other, 1)
            return Fraction(self.numerator, self.denominator) >= Fraction(new_other.numerator, new_other.denominator)
        else:
            raise TypeError('comparing with not a number')
    
    def __le__(self, other):
        if isinstance(other, Fraction) or isinstance(other, FractionExtended):
            return Fraction(self.numerator, self.denominator) <= Fraction(other.numerator, other.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            new_other = FractionExtended(other, 1)
            return Fraction(self.numerator, self.denominator) <= Fraction(new_other.numerator, new_other.denominator)
        else:
            raise TypeError('comparing with not a number')
