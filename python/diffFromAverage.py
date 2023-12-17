def differences_from_average(data):
    # Calculate the average of the data
    average = sum(data) / len(data)
    
    # Calculate the differences from the average and round to two decimal places
    differences = [round(average - x, 2) for x in data]
    
    return differences

# Example usage
data = [55, 95, 62, 36, 48]
result = differences_from_average(data)
print(result)
