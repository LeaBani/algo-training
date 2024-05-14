# Recherche du premier entier c tel que c et (p-1)(q-1) soient premiers entre eux

def c(p, q):  
    c=1  
    j=c+2  
    b=True  
    while b and j<(p-1)*(q-1):   
        i1=(p-1)*(q-1)   
        j1=j   
        k=2   
        while k>1:    
            k=i1%j1    
            i1=j1    
            j1=k   
        if k==0:
            j=j+2   
        else:    
            b=False  
            if b:   
                print("pas de c")  
            else:   
                c=j  
            print("le résultat est c = ",c) 

c(97, 109)

# Recherche d tel que c d ≡	[( − )( − )] 

def d(p, q, c):  
    i=1  
    while ( i % c ) != 0:   
        i= i + ( p - 1 )*( q - 1 )  
    d=i/c  
    print("d=",d) 

d(97, 109, 5)

# Calcul du reste de la division de ac (ou ad par n)

def b(a, c_ou_d, n):  
    b = 1  
    i = 1  
    while i <= c_ou_d:   
        b = b * a   
        b = b % n   
        i = i + 1  
    print("## message crypté, reste = b =", b) 

b(1410, 5, 10573)

# #Vérifie si un nombre est premier ou pas 

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

# premier() 

# # Recherche le nombre premier juste inférieur à n 

# def premier(n):  
#     nombre = n  
#     p=0  
#     s=True  
    
#     while s:   
#         print("Le programme est en train de vérifier si le nombre ",n-p," est premier...")   
#         i=2   
#         while i < nombre and nombre % i != 0:    
#             i = i + 1   
#         if i == nombre:    
#             print("Le nombre", nombre, "est premier ! Fantastique !")    
#             s=False   
#         else:    
#             p=p+1    
#             nombre=n-p 


# premier(700)

