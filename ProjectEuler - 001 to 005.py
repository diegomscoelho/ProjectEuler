#Soma dos múltiplos de 3 e 5 menores do que 1000 ?
#nothing -> int
def soma1000():
    soma3=0
    soma5=0
    soma15=0
    for i in range (3,1000,3):  #Soma dos múltiplos de 3 menores que 1000
        soma3+=i
    for p in range (5,1000,5):  #Soma dos múltiplos de 5 menores que 1000
        soma5+=p
    for x in range (15,1000,15): #Soma dos múltiplos de 15 menores que 1000
        soma15+=x
    total=soma3+soma5-soma15    #Os múltiplos de 15 estão repetidos
    return total

#Soma dos números pares da sequência de fibonacci até 4 milhões ?

def fibo2():
    f1=1
    f2=2
    soma=0
    while f2<4*10**6:   #enquanto o maior número de fibonacci for menor de 4 milhões a soma continua
        if f2%2==0: #todo número par é somado
            soma+=f2
        f1,f2=f2,f1+f2  #o número f1 vira o f2 e o f2 vira a soma f1 + f2
    return soma

#Maior fator primo do número 600851475143 ?
        
def MfatP(n):
    crivo=2
    while crivo<=n:     #Roda a função enquanto o crivo for menor ou igual a n.
        if n%crivo==0:  #Se o crivo dividir o n
            n=n/crivo   #Um novo n é gerado que é o n dividido pelo crivo
            if n==1:
                print "O maior é " + str(crivo) #Se o n dividido pelo crivo é igual não há outro número a dividir
                break   #Para a função final
            MfatP(n)    #Outra função é gerada com o novo crivo
            break       #Evita que entre novamente num número que é divisor
        crivo+=1

#Maior palíndromo feito pelo produto de dois números com 3 digitos cada ?

def rule_palin(x): #Existem 4 casos palindrómicos ou capicúas.
    if str(x)[:len(str(x))/2]==str(x)[len(str(x))/2:]:  #Numero com nº dígitos par, a primeira parte igual a segunda
        if str(x)[0]==str(x)[len(str(x))-1]:
            return True
    elif str(x)[len(str(x))/2+1:]==str(x)[:len(str(x))/2]:  #Numero com nº dígitos ímpar, a primeira parte igual a segunda
        if str(x)[0]==str(x)[len(str(x))-1]:
            return True
    elif str(x)[:len(str(x))/2]==str(x)[len(str(x))-1:len(str(x))/2:-1]:    #Numero com nº dígitos par, a primeira parte igual ao inverso da segunda
        if str(x)[0]==str(x)[len(str(x))-1]:
            return True
    elif str(x)[:len(str(x))/2]==str(x)[len(str(x))-1:len(str(x))/2-1:-1]:  #Numero com nº dígitos ímpar, a primeira parte igual ao inverso da segunda
        if str(x)[0]==str(x)[len(str(x))-1]:
            return True
        
def palin():
    Maior=1
    for a in range (100,1000):
        for b in range (100,1000):
            N=a*b
            if rule_palin(N)==True and Maior<N:
                Maior=N
    return Maior

#Menor número positivo que é divísel por (n naturais) de 1 a n com resto 0.
def listprime(n):                       #Função que dá a lista de primos de 2 a n
    from math import sqrt   
    primos=range(2,n+1)                 #lista de 2 a n
    limite=range(2,int(sqrt(n))+1)      #limite da exclusão (otimiza a função)
    for exc in limite:                  
        for numero in primos:
            if numero%exc==0 and numero!=exc: #Se o numero do limite dividir o numero do primo, ele é removido (excetuando quando o numero é ele mesmo)
                primos.remove(numero)
    return primos

def menormult(n):
    if n==1:
        return 1
    lista=listprime(n)
    mm=2
    for numero in range(2,n+1):
        if mm%numero!=0:
            for divisor in lista:
                if numero%divisor==0:
                    mm*=divisor
                    
    return mm



