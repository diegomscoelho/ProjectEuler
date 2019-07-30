#Soma dos m�ltiplos de 3 e 5 menores do que 1000 ?
#nothing -> int
def soma1000():
    soma3=0
    soma5=0
    soma15=0
    for i in range (3,1000,3):  #Soma dos m�ltiplos de 3 menores que 1000
        soma3+=i
    for p in range (5,1000,5):  #Soma dos m�ltiplos de 5 menores que 1000
        soma5+=p
    for x in range (15,1000,15): #Soma dos m�ltiplos de 15 menores que 1000
        soma15+=x
    total=soma3+soma5-soma15    #Os m�ltiplos de 15 est�o repetidos
    return total

#Soma dos n�meros pares da sequ�ncia de fibonacci at� 4 milh�es ?

def fibo2():
    f1=1
    f2=2
    soma=0
    while f2<4*10**6:   #enquanto o maior n�mero de fibonacci for menor de 4 milh�es a soma continua
        if f2%2==0: #todo n�mero par � somado
            soma+=f2
        f1,f2=f2,f1+f2  #o n�mero f1 vira o f2 e o f2 vira a soma f1 + f2
    return soma

#Maior fator primo do n�mero 600851475143 ?
        
def MfatP(n):
    crivo=2
    while crivo<=n:     #Roda a fun��o enquanto o crivo for menor ou igual a n.
        if n%crivo==0:  #Se o crivo dividir o n
            n=n/crivo   #Um novo n � gerado que � o n dividido pelo crivo
            if n==1:
                print "O maior � " + str(crivo) #Se o n dividido pelo crivo � igual n�o h� outro n�mero a dividir
                break   #Para a fun��o final
            MfatP(n)    #Outra fun��o � gerada com o novo crivo
            break       #Evita que entre novamente num n�mero que � divisor
        crivo+=1

#Maior pal�ndromo feito pelo produto de dois n�meros com 3 digitos cada ?

def rule_palin(x): #Existem 4 casos palindr�micos ou capic�as.
    if str(x)[:len(str(x))/2]==str(x)[len(str(x))/2:]:  #Numero com n� d�gitos par, a primeira parte igual a segunda
        if str(x)[0]==str(x)[len(str(x))-1]:
            return True
    elif str(x)[len(str(x))/2+1:]==str(x)[:len(str(x))/2]:  #Numero com n� d�gitos �mpar, a primeira parte igual a segunda
        if str(x)[0]==str(x)[len(str(x))-1]:
            return True
    elif str(x)[:len(str(x))/2]==str(x)[len(str(x))-1:len(str(x))/2:-1]:    #Numero com n� d�gitos par, a primeira parte igual ao inverso da segunda
        if str(x)[0]==str(x)[len(str(x))-1]:
            return True
    elif str(x)[:len(str(x))/2]==str(x)[len(str(x))-1:len(str(x))/2-1:-1]:  #Numero com n� d�gitos �mpar, a primeira parte igual ao inverso da segunda
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

#Menor n�mero positivo que � div�sel por (n naturais) de 1 a n com resto 0.
def listprime(n):                       #Fun��o que d� a lista de primos de 2 a n
    from math import sqrt   
    primos=range(2,n+1)                 #lista de 2 a n
    limite=range(2,int(sqrt(n))+1)      #limite da exclus�o (otimiza a fun��o)
    for exc in limite:                  
        for numero in primos:
            if numero%exc==0 and numero!=exc: #Se o numero do limite dividir o numero do primo, ele � removido (excetuando quando o numero � ele mesmo)
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



