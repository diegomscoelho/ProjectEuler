#Special Pythagorean triplet - Problem 9

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def findtriplet():
    from math import sqrt
    for b in range (2,999):
        for a in range (1,b):
            if sqrt(a**2+b**2)+a+b==1000 and b>a:
                return a*b*int(sqrt(a**2+b**2)),(a,b,int(sqrt(a**2+b**2)))
