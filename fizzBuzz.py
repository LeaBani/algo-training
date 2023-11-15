def reverse_fizz_buzz(list_of_numbers):
    new_list_of_numbers = []

    for index, char in enumerate(list_of_numbers):
        if char == "Fizz" or char == "Buzz":
            res = index+1
            new_list_of_numbers.append(res)

    print(tuple(new_list_of_numbers))

    return tuple(new_list_of_numbers) # tuple permet de représenter une paire ordonnée de valeurs en Python

list_of_numbers = [1,2,"Fizz",4,"Buzz"]
resultat = reverse_fizz_buzz(list_of_numbers)    
print(resultat) 