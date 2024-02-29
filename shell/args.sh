#!/bin/bash

# value=$1 
# echo "le carré de $value est $((value*value))"

# value1=$1 
# value2=$2

# echo "La somme de $value1 et $value2 et est $((value1+value2))"

# sum=0

# for element in "$@"; do
#     ((sum+=element))
# done

# echo "La somme des arguments est : $sum"

# for ((i=1; i<=$#; i++))
# do
#     ((sum+=${!i}))
# done

# max=0

# for element in "$@"; do
#     if ((max < $element)); then
#     ((max = $element));
#     fi
# done

# echo "La valeur max des arguments est : $max"

# result=$1
# arg=$1

# for element in "$@"; do

#     abs=$element;

#     if (($element < 0)); then
#         ((abs = $element*-1));
#     fi

#     if ((result > $abs )); then
#     ((result = $abs));
#     ((arg = $element));
#     fi
# done

# echo "La valeur la plus proche de zéro est : $arg "

result=$1
arg=$1

for element in "$@"; do

    abs=$element;

    if (($element < 0)); then
        ((abs = $element*-1));
    fi

    if ((result > $abs)) && ((element=$abs)) ; then
    ((result = $abs));
    ((arg = $element));
    fi
    
done

echo "La valeur la plus proche de zéro est, en prenant la valeur positive si égalité entre deux arguments : $arg "
