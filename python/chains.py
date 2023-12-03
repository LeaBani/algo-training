s1 = "+-++--"
s2 = "++---+"

def neutralise(s1, s2):
 
    result = ""

    my_list = list(result)


    # ici je veux comparer les char de mes 2 string
    for char1, char2 in zip(s1, s2):
        if char1 == "+" and char2 == "+":
            result = "+"
            # j'ajoute mon résultat à ma liste
            my_list.append(result)
            
        elif char1 == "-" and char2 == "-":
            result = "-"
            my_list.append(result)

        else :
            result = "0"
            my_list.append(result)

    return ''.join(my_list) # je recréé une chaine de charactères

resultat = neutralise(s1, s2)
print(resultat)
