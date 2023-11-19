def reverse_fizz_buzz(list_of_numbers):
    new_list_of_numbers = []
    fizz_buzz = True

    for index, char in enumerate(list_of_numbers):
        if char == "FizzBuzz" and fizz_buzz:
            res = index +1 
            fizz_buzz = False 
            new_list_of_numbers.append(res)    
            # print(new_list_of_numbers)
        elif char == "FizzBuzz" and not fizz_buzz: 
            resp = index +1 
            if resp % res == 0:
                new_list_of_numbers.append(res) 
            else:
                fizz_buzz = False 
                new_list_of_numbers.append(resp)    
                print(new_list_of_numbers)


    return tuple(new_list_of_numbers) 



    # for index, char in enumerate(list_of_numbers):
    #     if char == "Fizz" or char == "Buzz":
    #         res = index+1
    #         new_list_of_numbers.append(res)


    # tuple permet de représenter une paire ordonnée de valeurs en Python

list_of_numbers = [1,"FizzBuzz",3,"FizzBuzz",5,"FizzBuzz"]
resultat = reverse_fizz_buzz(list_of_numbers)    
print(resultat) 



