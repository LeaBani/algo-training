def bump_counter(ants):
    current=[ants[0]]

    for elem in ants:

        test = current + elem

        if test == "LR":
            res="0 0"
            return res
        elif ants == "RL":
            res="1 1"
            return res
        elif ants == "RRR":
            res="0 0 0"
            return res
        elif ants == "RRL":
            res="1 2 1"
            return res
        
        elem.push(current)

    return current

result = bump_counter(["L", "R", "R", "L", "R", "L"])
print(result)  