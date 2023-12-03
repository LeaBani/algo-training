def greatest_product(st):
    max_product = 0 # initialise variable

    for i in range(len(st) - 4):
        current_product = int(st[i]) * int(st[i + 1]) * int(st[i + 2]) * int(st[i + 3]) * int(st[i + 4]) # calculate product from 4 integer 
        max_product = max(max_product, current_product)

    return max_product

result = greatest_product("123834539327238239583")
print(result)  
