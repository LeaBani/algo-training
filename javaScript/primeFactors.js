/**
 * Cette fonction permet de recherche les facteurs premiers d'un nombre
 * @param {integer} n l'entier pour lequel on recherche la décomposition en facteur premier
 * @returns un tableau avec les nombres
 */
function primeFactors(n) {
    // j'initialise mon tableau vide pour stocker mes facteurs
    const factors = [];
    // j'intialise mon premier diviseur a 2 (règle des nb premiers)
    let divisor = 2;

    // je boucle si n est sup ou égla à 2
    while (n >= 2) {

        // si le reste de la division euclidienne est égale a 0
      if (n % divisor === 0) {
        // j'ajoute à mon tableau de facteurs le diviseur
        factors.push(divisor);

        // j'actualise donc mon n soit le reste de ma division
        n = n / divisor; // 2563
        //console.log("divi", divisor);
      } else {
        // sinon j'incrémente mon diviseur
        divisor++;
      }
    }
    console.log("factors", factors)
    return factors;
  }
  
  // test avec un nombre aléatoire
  const randomNumber = Math.floor(Math.random() * 10000);
  console.log('Prime factors of', randomNumber + ':', primeFactors(randomNumber).join(' '))