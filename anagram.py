from collections import Counter

def anagram_counter(words):
    # Helper function to convert a word to its sorted form (method sorted)
    def sort_word(word):
        return ''.join(sorted(word))

    # Use Counter to count occurrences of sorted words
    sorted_word_counts = Counter(map(sort_word, words))
    print(sorted_word_counts.values())

    # Calculate the number of pairs using nC2 formula - C(n,2)= n! / 2!*(n−2)! - "//" is the floor division operator

    total_pairs = sum(count * (count - 1) // 2 for count in sorted_word_counts.values())

    return total_pairs

result = anagram_counter(['dell', 'ledl', 'abc', 'cba', 'bca', 'bac', 'cab'])
print(result)