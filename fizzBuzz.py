def reverse_fizz_buzz(list_of_numbers):
    new_list_of_numbers = []
    new_array = []

    fizz_found = False
    buzz_found = False

    for index, char in enumerate(list_of_numbers):
        if char == "Fizz" and not fizz_found:
            fizz = index + 1
            new_list_of_numbers.append(fizz)
            fizz_found = True
        elif char == "Buzz" and not buzz_found:
            buzz = index + 1
            new_list_of_numbers.append(buzz)
            buzz_found = True
        elif char == "Fizz" and fizz_found or char == "Buzz" and buzz_found:
            res = index + 1
            new_array.append(res)
        elif char == "FizzBuzz" and not buzz_found:
            fizz_buzz = fizz * new_array[-1] + 1
            new_list_of_numbers.append(fizz_buzz)
            # print(fizz_buzz)

            
    return tuple(new_list_of_numbers) 



    # for index, char in enumerate(list_of_numbers):
    #     if char == "Fizz" or char == "Buzz":
    #         res = index+1
    #         new_list_of_numbers.append(res)


    # tuple permet de représenter une paire ordonnée de valeurs en Python

list_of_numbers = [1,"FizzBuzz",3,"FizzBuzz",5,"FizzBuzz"]
resultat = reverse_fizz_buzz(list_of_numbers)    
print(resultat) 


