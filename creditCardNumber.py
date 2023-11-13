def validate(n):
    n_str = str(n)

    # Créer une liste pour stocker chaque chiffre
    n_array = []

    # Itérer sur chaque caractère de la chaîne et le convertir en entier
    for char in n_str:
        n_int = int(char)

        # si le nombre est pair alors le multiplier par 2 
        if n_int % 2 != 0:
            if n_int*2 > 9:
                res = n_int*2 - 9
                n_array.append(res)
            else:
                n_array.append(n_int)
        else:
            n_array.append(n_int)

    if sum(n_array) % 10 != 0:
        return False
    else: 
        return True

n = 1230
resultat = validate(n)    
print(resultat) 