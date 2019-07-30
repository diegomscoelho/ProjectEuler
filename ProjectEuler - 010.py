#Summation of primes - Problem 10
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def primesome(n):
    from math import sqrt
    prime=[]
    num=2
    while n>num:              #Enquanto o tamanho da lista não atingir o n, ela não para. Começa em 2 (num).
        primalidade=True
        for i in range(2,int(sqrt(num))+1): #Gera os números que vão testar a primalidade do número
            if num%i==0:                    #Verifica se o número é primo
                primalidade=False
        if primalidade==True:               #Se o número é primo, ele é adicionado na lista
            prime.append(num)
        num+=1                              #Número adjacente será testado
    return sum(prime)                       #A respota é a soma de todos os primos abaixo de n.
