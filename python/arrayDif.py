def array_diff(a, b):
    # here we solve the problem using not in operator. It permits to filter from array a
    # we create a new_array
    new_array = [x for x in a if x not in b]
    return new_array

result = array_diff([1,2,3], [1, 2])
print(result)