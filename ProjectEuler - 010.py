#Summation of primes - Problem 10
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def primesome(n):
    from math import sqrt
    prime=[]
    num=2
    while n>num:              #Enquanto o tamanho da lista n�o atingir o n, ela n�o para. Come�a em 2 (num).
        primalidade=True
        for i in range(2,int(sqrt(num))+1): #Gera os n�meros que v�o testar a primalidade do n�mero
            if num%i==0:                    #Verifica se o n�mero � primo
                primalidade=False
        if primalidade==True:               #Se o n�mero � primo, ele � adicionado na lista
            prime.append(num)
        num+=1                              #N�mero adjacente ser� testado
    return sum(prime)                       #A respota � a soma de todos os primos abaixo de n.
