from math import *  

## VERSION 1
def premier(n) : 

    if n<=1:   
        return(False) 
    
    i=2  
    b=int(sqrt(n))+1 # vérification pour n=2
    while i<b and n%i !=0:   
        i+=1 

    while i<n and n%i !=0:   i+=1  
    if i==n:   
        return(True)  
    else:   
        return(False)


def rechprem(n):  
    p=0  
    s=True  
    while s:   
        if premier(n-p)==True:    
            s=False   
        p+=1  
    print(n-p+1,"est le premier nombre premier inférieur ou égal à", n)  
        

# resultat = premier(1000000)
# print(resultat) 

rechprem(100)

## VERSION 2

# def premier(): 
#     nombre = input("Écris un nombre entier positif : ") 
#     nombre = int(nombre) 
#     print("Le programme est en train de vérifier si ce nombre est premier...") 
#     i=2 
#     while i < nombre and nombre % i != 0: 
#         i = i + 1 
#     if i == nombre: 
#         print("Le nombre", nombre, "est premier ! Fantastique !") 
#     else: 
#         print("Ce n'est pas un nombre premier.") 

# resultat = premier()
# print(resultat) 