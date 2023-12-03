def first_non_repeating_letter(s):

# Convert the string to lowercase to handle case-insensitivity
    string_lower = s.lower()

    # Iterate through each character in the string
    for char in s:
        # Check if the lowercase version of the character appears only once in the string
        if string_lower.count(char.lower()) == 1:
            return char

    # If no non-repeating character is found, return an empty string or None
    return ""

result = first_non_repeating_letter('abba')
print(result)