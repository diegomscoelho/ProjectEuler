#10001st prime - Problem 7
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

def primefinder(n):
    from math import sqrt
    prime=[]
    num=2
    while n!=len(prime):                    #Enquanto o tamanho da lista não atingir o n'ésimo primo, ela não para
        primalidade=True
        for i in range(2,int(sqrt(num))+1): #Gera os números que vão testar a primalidade do número
            if num%i==0:                    #Verifica se o número é primo
                primalidade=False
        if primalidade==True:               #Se o número é primo, ele é adicionado na lista
            prime.append(num)
        num+=1                              #Número adjacente será testado
    return prime[len(prime)-1]              #A respota é o n'ésimo número primo
