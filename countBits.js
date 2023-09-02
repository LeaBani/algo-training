
/**
 * Je veux compter le nombre de 1 dans l'écriture binaire du nombre n
 * @param {integer} n le nombre a convertir en binaire
 * @returns le nombre de 1 dans ce nombre
 */
var countBits = function(n) {

    // je converti n en binaire
    const nBinary = n.toString(2);
    console.log(nBinary)

    // je sépare chaque item et j'obtiens un tableau
    const eachOne = nBinary.split("");
    // console.log("eachOne", eachOne)

    /**
     * Ici je créé une fonction permettant d'effectuer un filtre sur les 1
     * @param {integer} element est soit 1 soit 0 (binaire)
     * @returns tous les éléments qui sont égaux à 1
    */
   function isOne(element) {
       return element === "1";
    }
    
    // je filtre mon tableau eachOne pour chaque item qui est égal a 1 et j'obtiens la longueur de ce tableau
      const numberOfOnes = eachOne.filter(isOne).length;
      console.log("numberOfOnes", numberOfOnes)

      return numberOfOnes;
    
  };

countBits(5302988069)