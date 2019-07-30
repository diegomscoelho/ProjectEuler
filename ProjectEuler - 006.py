# Sum square difference - Problem 6
'''
Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.
'''

def difsquare(n):
    sumsq=0
    sqsum=0
    for num in range(1,n+1):
        sumsq+=num**2
        sqsum+=num
    return sqsum**2-sumsq
