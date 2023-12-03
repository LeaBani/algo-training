function findEvenIndex(arr)
{
  // Je cherche l'index N ou la somme des entiers à gauche de N et égale à la somme des entiers à droite de N
  // si il n'y a pas d'égalité, on retourne -1


    // je somme

    const initialValue = 0;

    const arrReverse = []
    const arrInit = []
    //console.log(arrReverse)

        arr.reduce(function (accumulator, currentItem, index) {
            const sum = accumulator + currentItem;
            arrInit.push([sum, index])
            // console.log(sum, index)
            return sum;
        }, initialValue);
    
            
        arr.reduceRight(function (accumulator, currentItem, index) {
            const sum = accumulator + currentItem;
            // console.log(sumRight, index)
            arrReverse.push([sum, index])
            return sum;
        }, initialValue);

        // console.log("arr init", arrInit)
        // console.log("arr reverse", arrReverse)

        const convArrayReverse = JSON.stringify(arrReverse);
        // console.log("test", convArrayReverse)
        console.log("test", arrInit)

        // je compare les deux tableau et recherche la premiere valeur en commun
        
        const isEqualTo = (element) => {
            const isFound = convArrayReverse.includes(element)
            console.log("isFound", isFound)
            //console.log("elem", element)
            console.log("arr", convArrayReverse)

                return isFound;
        };

        const result = arrInit.findIndex(isEqualTo);
        console.log("result", result)

        return result;

        // if (result !== undefined) {
        //     //console.log("result", result);
        //     return result;
            
        // } else {
        //     //console.log("result is neg", -1)
        //     return -1;  
        // }

}



findEvenIndex([1,2,3,4,3,2,1])
