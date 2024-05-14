def permutations(s):
    if len(s) <= 1:
        return [s]
    
    perms = set()
    for i, char in enumerate(s):
        for perm in permutations(s[:i] + s[i+1:]):
            perms.add(char + perm)
    
    return list(perms)

# Test cases
print(permutations('a'))   # ['a']
print(permutations('ab'))  # ['ab', 'ba']
print(permutations('abc')) # ['bac', 'abc', 'acb', 'bca', 'cba', 'cab']
print(permutations('aabb'))# ['baba', 'abab', 'bbaa', 'aabb', 'abba', 'baab']

