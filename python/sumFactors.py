# # " Sieve of Erathosthene ": générer la liste des nombres premiers
# def primes_slice(limit):
#     is_prime = [False] * 2 + [True] * (limit - 1) 
#     for n in range(int(limit**0.5 + 1.5)): 
#         if is_prime[n]:
#             for i in range(n*n, limit+1, n):
#                 is_prime[i] = False
#     return [i for i, prime in enumerate(is_prime) if prime]

# def sum_for_list(lst):

#     prime_of_lst = []
#     for element in lst:
#         primes = primes_slice(abs(element))
#         # print('primes', primes)

#         for prime in primes:
#             if element % prime != 0:
#                 False
#             else:
#                 prime_of_lst.append([prime, element])

#     # print('prime of lst', prime_of_lst)
#     res_array = sum_result(prime_of_lst)

#     return sorted(res_array)

# def sum_result(lst):
    
#     sums_dict = {}

#     for pair in lst:
#         first_value, second_value = pair

#         # Update the sum for the current first value
#         if first_value in sums_dict:
#             sums_dict[first_value] += second_value
#         else:
#             sums_dict[first_value] = second_value

#     # Convert the dictionary back to a list of pairs
#     result_array = [[key, value] for key, value in sums_dict.items()]
#     # print(result_array)

#     return result_array



# data = [15,21,24,30,-45]
# result = sum_for_list(data)
# print(result)

def primes_slice(limit):
    is_prime = set(range(2, limit + 1))
    for n in range(2, int(limit**0.5) + 1):
        if n in is_prime:
            is_prime.difference_update(range(n * n, limit + 1, n))
    return list(is_prime)

def sum_for_list(lst):
    prime_of_lst = []
    for element in lst:
        primes = primes_slice(abs(element))
        for prime in primes:
            if element % prime == 0:
                prime_of_lst.append([prime, element])
    res_array = sum_result(prime_of_lst)
    return sorted(res_array)

def sum_result(lst):
    sums_dict = {}
    for pair in lst:
        first_value, second_value = pair
        sums_dict[first_value] = sums_dict.get(first_value, 0) + second_value
    return [[key, value] for key, value in sums_dict.items()]

# Example usage:
data = [15,21,24,30,-45]
result = sum_for_list(data)
print(result)
