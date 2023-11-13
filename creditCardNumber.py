def validate(n):
    n_str = str(n)

    # Créer une liste pour stocker chaque chiffre
    n_array = []

    # Itérer sur chaque caractère de la chaîne et le convertir en entier
    for chiffre_char in n_str:
        chiffre_int = int(chiffre_char)

        # si le nombre est pair alors le multiplier par 2 
        if chiffre_int % 2 == 0:
            n_array.append(chiffre_int*2)
        else:
            n_array.append(chiffre_int)

        
        print(n_array)
        
n = 1714
resultat = validate(n)    
print(resultat) 