def parse_time(time_str):
    # here I convert my data in time (seconds)
    h, m, s = map(int, time_str.split('|'))
    return h * 3600 + m * 60 + s

def format_time(seconds):
    h, rem = divmod(seconds, 3600) # h = hours after divison by 3600, rem = remainder of this calculation
    m, s = divmod(rem, 60) # m = minutes, result of the division of rem/60, s = remainder of this calculation, so the seconds
    return f"{h:02d}|{m:02d}|{s:02d}"

def stat_team(race_results):
    if not race_results:
        return ""

    race_times = [parse_time(time) for time in race_results.split(', ')]

    # Calculate range from the array of parsed data max - min
    range_time = max(race_times) - min(race_times)
    # print('range time', range_time)

    # Calculate average
    average_time = sum(race_times) // len(race_times) # floor operation operator

    # Calculate median
    sorted_times = sorted(race_times)
    n = len(sorted_times)
    if n % 2 == 0:
        median_time = (sorted_times[n // 2 - 1] + sorted_times[n // 2]) // 2
    else:
        median_time = sorted_times[n // 2]

    # Expected format in kata
    result_str = f"Range: {format_time(range_time)} Average: {format_time(average_time)} Median: {format_time(median_time)}"
    return result_str

race_results = "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"
result = stat_team(race_results)
print(result)
