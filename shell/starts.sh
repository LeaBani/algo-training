#!/bin/bash

echo "Combien d'étoiles ?"
read value

for ((i=1; i<=value; i++))
do
    for ((j=1; j<=value; j++))
    do
        echo -n "*"
    done
    echo ""
done

# echo "Combien d'étoiles ?"
# read value

# for ((i=1; i<=value; i++))
# do
#     for ((j=1; j<=i; j++))
#     do
#         echo -n "*"
#     done
#     echo ""
# done

# echo "Combien d'étoiles ?"
# read value

# for ((i=value; i>=1; i--))
# do
#     for ((j=1; j<=i; j++))
#     do
#         echo -n "*"
#     done
#     echo ""
# done

# echo "Combien d'étoiles ?"
# read value

# for ((i=value; i>=1; i--))
# do
#     for ((j=1; j<=i; j++))
#     do
#         echo -n "+"
#     done
#     for ((j=value; j>=i; j--))
#     do
#         echo -n "*"
#     done
#     echo ""
# done

# echo "Combien d'étoiles ?"
# read value

# for ((i=1; i<=value; i++))
# do
#     for ((j=1; j<=i; j++))
#     do
#         echo -n "* "
#     done
#     echo ""
# done

# echo "Combien d'étoiles ?"
# read value

# for (( i=0 ; i<value ; i++ )); do 
#     echo -n "*"
# done 
#     echo ""

# for ((i=2; i<=value-1; i++))
# do
#     echo -n "*"

#     for ((j=1; j<=value-2; j++))
#     do
#         echo -n " "
#     done

#     for ((j=1; j>=1; j--))
#     do
#         echo -n "*"
#     done
#     echo ""
# done

# for ((i=1; i<=value; i++))
# do
# echo -n "*"
# done

# echo "Vous souhaitez la table de quelle valeur ?"
# read value

# for ((i=1; i<=10; i++))
# do
# echo -n $value*$i=$((value*i))
# echo ""
# done
