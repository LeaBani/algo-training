# def sum_of_intervals(intervals):

#     sum_of_length = []

#     for char in intervals:
#         length_of_intervals = char[1]-char[0]

#     print(sum_of_length)

# def sum_of_intervals(intervals):
#     # Sort the intervals
#     sorted_intervals = sorted(intervals)

#     # Initialize variables to keep track of the current interval and the total sum
#     total_sum = 0

   
#     for interval in sorted_intervals:

#         length_of_intervals = interval[1]-interval[0]
#         total_sum += length_of_intervals

#     return total_sum

# result = sum_of_intervals([(6, 10), (1, 9)])
# print(result)  

def merge_overlapping_intervals(intervals):
    # Sort the intervals
    sorted_intervals = sorted(intervals)

    # Initialize variables to keep track of the merged intervals
    merged_intervals = [sorted_intervals[0]]

    # Iterate through the sorted intervals and merge overlapping ones
    for interval in sorted_intervals[1:]: # this semantic helps to loop on the list from index 1
        if merged_intervals[-1][1] >= interval[0]:
            # print(merged_intervals[-1][1])  # last value in the interval
            # print(merged_intervals[-1])     # interval
            # print(merged_intervals[-1][0])  # first value in the interval

            # Merge
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
        else:
            # Add non-overlapping interval
            merged_intervals.append(interval)

    return merged_intervals

def sum_of_intervals(intervals):
    # Merge overlapping intervals
    merged_intervals = merge_overlapping_intervals(intervals)
    print(merged_intervals)

    total_sum = 0

    # Calculate the total sum of the merged intervals (first solution)
    # total_sum = sum(end - start for start, end in merged_intervals)

    # second solution
    for interval in merged_intervals:

        length_of_intervals = interval[1]-interval[0]
        total_sum += length_of_intervals

    return total_sum

result = sum_of_intervals([(1, 4), (1, 6)])
print(result)