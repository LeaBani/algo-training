def count_characters(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1 # get permets d'aller chercher dans la string char_count et renvoie la valeur de celle ci. 
        # 0 est la valeur par défaut. On incrémente alors pour compter le nombre d'occurences de chaque element

    return char_count

# Example usage
s = "aba"
result = count_characters(s)
print(result)
