def array_diff(a, b):
    new_array = []

    if a == [] or b == []:
        return a
    
    for i in a:
        if i != b[0]:
            new_array.append(i)
    return new_array

result = array_diff([1,2,2], [])
print(result)