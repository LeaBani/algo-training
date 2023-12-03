def alphabet_position(text): # utilisation de la méthode ord pour assigner a un char sa position dans l'alphabet

    result = []
    for char in text:
        if 'a' <= char <= 'z':
            position = ord(char) - ord('a') + 1
            result.append(str(position))
        elif 'A' <= char <= 'Z':
            position = ord(char) - ord('A') + 1
            result.append(str(position))
        
    return ' '.join(result)

texte = "The sunset sets at twelve o' clock."
resultat = alphabet_position(texte)    
print(resultat) 
