def validate(n):
    n_str = str(n)

    # Créer une liste pour stocker chaque chiffre
    n_array = []

    # Itérer sur chaque caractère de la chaîne et le convertir en entier
    for index, char in enumerate(n_str):
        n_int = int(char)

        # Si la longueur de n est paire, doubler chaque deuxième chiffre, sinon, doubler chaque deuxième chiffre à partir du deuxième
        if len(n_str) % 2 == 0:
            if index % 2 == 0:
                double = n_int * 2
                if double > 9:
                    res = double - 9
                    n_array.append(res)
                else:
                    n_array.append(double)
            else:
                n_array.append(n_int)
        else:
            if index % 2 != 0:
                double = n_int * 2
                if double > 9:
                    res = double - 9
                    n_array.append(res)
                else:
                    n_array.append(double)
            else:
                n_array.append(n_int)

    print(n_array)
    print(sum(n_array) % 10)
    if sum(n_array) % 10 != 0:
        return False
    else: 
        return True

n = 1714
resultat = validate(n)    
print(resultat) 