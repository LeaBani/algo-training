def create_phone_number(n):
    
    if len(n) != 10:
        return "Le tableau doit contenir 10 chiffres."

    formatted_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*n) # avec la methode format, je peux formatter mon tableau
        
    return formatted_number

resultat = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(resultat) # "(123) 456-7890"