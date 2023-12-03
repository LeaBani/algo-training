// test

// le nombre de fois de chaque élement dans le tableau, non sensible a la casse

function testArray(array) {

    // const newArray= [];
    // const newObj ={};


    // for (const element of array) {
    //     const word = element.toLowerCase();
    //     console.log(newObj.hasOwnProperty(word));

    //     if (newObj.hasOwnProperty(word) === true) {
    //         // incrémente
    //         newObj[word] = newObj[word] + 1;
            
    //     } else {
    //         // j'ajoute le word dans l'objet
    //         newObj[word] = 1;
            
    //     }
        
    //     console.log(newObj);

    // }

    // Input

    let newArray = [];

    Array.prototype.countCertainElements = function(value){
        console.log(value)
        return this.filter(newArray => newArray === value).length
    }


    for (const element of array) {
        const word = element.toLowerCase();
        newArray.push(word)
    }

    // console.log(newArray)

    for (const element of newArray) {
        const countElem = newArray.countCertainElements(element);
        // console.log(newArray)
        console.log({ elem: element, count: countElem})
    }
    

}

testArray(["Bonjour", "bonjour", "Hello", "Hello", "ciao","HELLO"]);


// class Arbre {

//     constructor(valeur, leftNode, rightNode) {
//       this.valeur = valeur;
//       this.leftNode = leftNode;
//       this.rightNode = rightNode;
//     }

    
//   }

// function countD (arbre) {
//     if (arbre.leftNode === null && arbre.rightNode === null) {
//         return 1;
//     }
//     if (arbre.leftNode === null) {
//         return countD(arbre.rightNode) +1;
//     }
//     if (arbre.rightNode === null) {
//         return countD(arbre.leftNode) +1;
//     }

//     console.log(Math.max(countD(arbre.rightNode) +1, countD(arbre.leftNode) +1));
// }

// countD(3)