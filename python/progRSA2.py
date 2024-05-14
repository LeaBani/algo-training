from math import * 

def premier(n) :  
    if n<=1:   
        return(False)  
    i=2  
    b=int(sqrt(n))+1  
    while i<b and n%i !=0:   
        i+=1  
    if i==b :   
        return(True)  
    else:   
        return(False) 
    
resultat = premier(1123)
print("prem", resultat) 

# def rechprem(n):  
#     p=0  
#     s=True  
#     while s:   
#         if premier(n-p)==True:    
#             s=False  
#         p+=1  
#     return(n-p+1)

# resultat = rechprem(10*20)
# print("rechprem", resultat) 

def decomp(n):  
    s=True  
    i=2  
    while s:   
        if premier(i)==True:    
            if n%i == 0:     
                q=n/i     
                p=i     
                if premier(q)==True:      
                    print("n = ",n," = p x q = ",p,"x",q)      
                    s=False   
        i+=1 

resultat =  decomp(99991)
print("decomp", resultat) 

from time import time 

def dureedecomp(n) :    
    debut = time()  # nombre de secondes depuis le 1er janvier 1970    
    decomp(n)   
    fin = time()     
    duree = fin-debut    
    print("durée du calcul pour obtenir la décomposition : ", duree)


dureedecomp(10**15) 

