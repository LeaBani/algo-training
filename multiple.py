def solution(number):
    # Check if the number is negative
    if number < 0:
        return 0

    # Initialize sum
    total_sum = 0

    # Iterate through numbers below the given number with range method
    for i in range(number):
        # Check if the current number is a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    return total_sum

result = solution(5)
print(result)