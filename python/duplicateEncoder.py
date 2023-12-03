def duplicate_encode(word):

# Convert the word to lowercase for case-insensitive comparison
    word_lower = word.lower()

    # Use a list comprehension to construct the new string (if char is duplicate so ')')
    result = ['(' if word_lower.count(char.lower()) == 1 else ')' for char in word]

    # Join the list of characters into a string
    return ''.join(result)

result = duplicate_encode('din')
print(result)