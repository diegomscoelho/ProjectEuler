#10001st prime - Problem 7
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

def primefinder(n):
    from math import sqrt
    prime=[]
    num=2
    while n!=len(prime):                    #Enquanto o tamanho da lista n�o atingir o n'�simo primo, ela n�o para
        primalidade=True
        for i in range(2,int(sqrt(num))+1): #Gera os n�meros que v�o testar a primalidade do n�mero
            if num%i==0:                    #Verifica se o n�mero � primo
                primalidade=False
        if primalidade==True:               #Se o n�mero � primo, ele � adicionado na lista
            prime.append(num)
        num+=1                              #N�mero adjacente ser� testado
    return prime[len(prime)-1]              #A respota � o n'�simo n�mero primo
