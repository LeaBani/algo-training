def spin_around(lst):
    my_sum = 0
    
    for element in lst:
        if element == "right":
            my_sum += 0.25
        else: 
            my_sum -= 0.25

    return int(abs(my_sum))

resultat = spin_around(['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'])
print(resultat)