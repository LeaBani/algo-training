# def find_emirp(n):
    
#     return [0, 0, 0]

# j'inverse n
# def reverse_num(n):
#     reverse = int(str(n)[::-1])
#     print(reverse)
#     return reverse

# je génère les nombres premiers jusqu'à n
# def generate_primes_up_to_n(n):
#     primes = set() # je créé un ensemble de données
#     is_prime = [True] * (n + 1)
#     for num in range(2, n + 1):
#         if is_prime[num]:
#             primes.add(num) # j'ajoute a mon set le num si il n'existe pas déjà
#             for multiple in range(num * num, n + 1, num):
#                 is_prime[multiple] = False
#     print(primes)
#     return primes

# " Sieve of Erathosthene ": générer la liste des nombres premiers
def primes_slice(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_emirps(n):
    primes = primes_slice(n)
    print(primes)
    emirps = []
    for prime in primes:
        reversed_prime = int(str(prime)[::-1]) # je renvoie la valeur inversée de chaque num
        if prime != reversed_prime: # si la valeur n'existe pas dans le set de données, je l'ajoute 
            test = is_prime(reversed_prime) # je teste si le nombre est un nombre premier
            # print(test, reversed_prime)
            if test == True:
                emirps.append(prime) #si oui , je l'ajoute à mon tableau d'emiprs
        
    # print(emirps)
    # print([len(emirps), max(emirps), sum(emirps)])
    return [len(emirps), max(emirps), sum(emirps)]

n = 50
result = find_emirps(n)
# print(result)