def reverse_fizz_buzz(list_of_numbers):
    new_list_of_numbers = []

    for index, char in enumerate(list_of_numbers):
        if char == "Fizz":
            res = index+1
            new_list_of_numbers.append(res)
        elif char == "Buzz":
            res = index+1
            new_list_of_numbers.append(res)

            print(new_list_of_numbers)

list_of_numbers = [1,"FizzBuzz",3,"FizzBuzz",5,"FizzBuzz"]
resultat = reverse_fizz_buzz(list_of_numbers)    
print(resultat) 