#Highly divisible triangular number - Problem 12#

def triangdiv(k):
    n=[1,1] #numero triangular, ordem numero triangular
    count=0
    while True:
        for i in range(1,n[0]+1):
            if n[0]%i:
               count+=1
        print(count)
        if k==count:
            return n[0]
        count=0
        n[1]+=1
        n[0]+=n[1]
    return n[0]
    
    
