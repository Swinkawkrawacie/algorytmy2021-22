def find_lcm(first:int, second:int):
    """
    Find the least common mul...
    """
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
    Find the greatest common factor
    """
    if first > second:
        bigger = first
        smaller = second
    elif first == second:
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
    def __init__(self, numerator:int, denominator:int):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        if denominator < 0:
            numerator *= -1
            denominator *= -1
        elif denominator == 0:
            raise ValueError
        common = find_gcf(denominator, numerator)
        self.numerator = int(numerator/common)
        self.denominator = int(denominator/common)
    
    def __str__(self):
        common = find_gcf(self.denominator, self.numerator)
        return str(int(self.numerator/common))+'/'+str(int(self.denominator/common))
    
    def __add__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator+other.numerator,self.denominator)
        else:
            common = find_lcm(self.denominator, other.denominator)
            first_mul = common/self.denominator
            second_mul = common/other.denominator
            return Fraction(int(first_mul*self.numerator+second_mul*other.numerator), common)
    def __sub__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator-other.numerator,self.denominator)
        else:
            common = find_lcm(self.denominator, other.denominator)
            first_mul = common/self.denominator
            second_mul = common/other.denominator
            return Fraction(int(first_mul*self.numerator-second_mul*other.numerator), common)

    def __mul__(self, other):
        return Fraction(int(self.numerator*other.numerator), int(self.denominator*other.denominator))

    def __truediv__(self, other):
        return Fraction(int(self.numerator*other.denominator), int(self.denominator*other.numerator))

    def getNum(self):
        return self.numerator

    def getDem(self):
        return self.denominator
    
    def __eq__(self, other):
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False
    
    def __ne__(self, other):
        return not(self==other)

    def __gt__(self, other):
        common = find_lcm(self.denominator, other.denominator)
        first_mul = common/self.denominator
        second_mul = common/other.denominator
        if self.numerator*first_mul > other.numerator*second_mul:
            return True
        else:
            return False
    
    def __lt__(self, other):
        common = find_lcm(self.denominator, other.denominator)
        first_mul = common/self.denominator
        second_mul = common/other.denominator
        if self.numerator*first_mul < other.numerator*second_mul:
            return True
        else:
            return False
    
    def __ge__(self, other):
        common = find_lcm(self.denominator, other.denominator)
        first_mul = common/self.denominator
        second_mul = common/other.denominator
        if self.numerator*first_mul >= other.numerator*second_mul:
            return True
        else:
            return False
    
    def __le__(self, other):
        common = find_lcm(self.denominator, other.denominator)
        first_mul = common/self.denominator
        second_mul = common/other.denominator
        if self.numerator*first_mul <= other.numerator*second_mul:
            return True
        else:
            return False


print(Fraction(2,4))
print(str(Fraction(3,5)))
print(Fraction(1,3)+Fraction(1,2))
print(Fraction(2,3)*Fraction(1,2))
print(Fraction(2,3)/Fraction(1,2))

print(Fraction(2,3)==Fraction(1,2))
print(Fraction(2,3)!=Fraction(1,2))
print(Fraction(2,3)==Fraction(2,3))
print(Fraction(2,3)!=Fraction(2,3))
print(Fraction(2,3)>Fraction(1,2))
print(Fraction(2,3)<Fraction(1,2))
print(Fraction(2,3)>=Fraction(1,2))
print(Fraction(2,3)<=Fraction(1,2))

print(Fraction(-2,3)==Fraction(2,3))
print(Fraction(-2,3)!=Fraction(2,3))
print(Fraction(2,3)<Fraction(-1,2))
print(Fraction(-2,3)<Fraction(1,2))

print(Fraction(2,-3)==Fraction(2,3))
print(Fraction(-2,-3)!=Fraction(2,3))
print(Fraction(2,-3)<Fraction(-1,2))
print(Fraction(-2,-3)<Fraction(1,2))

a = Fraction(2,3)
print(a)
print(a.getDem())
print(a.getNum())