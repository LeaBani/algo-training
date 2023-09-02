function spinWords(string){
    // console.log(string)
    
      // on inclue les espaces quand + de un mot uniquement
      
      // je veux créer une nouvelle string
      const newString = [];
      
      // je split le nombre de mots de ma string
      const words = string.split(' ');
      //console.log("words", words) // je récupère un tableau
      
      // je compte le nombre de lettre pour chaque mot du tableau obtenu
     
        for(const letters of words){
           // elem.length // me retourne la longueur de chaque mot du tableau
          
      // je cherche à inverser les mots qui ont plus de 5 lettres 
      
            if (letters.length > 4) {
                // je décompose les lettres
    
                    let letter = letters.split("");
                    // console.log("letter", letter)
                    // j'inverse l'ordre des lettres
                    let reverse = letter.reverse();
                    // console.log("reverse", reverse)
                    // je recupère la chaine de caractères obtenue
                    let value = reverse.join("");
                    // console.log(value)
                    newString.push(value);
            } else {
                newString.push(letters);
            }
} 
        let output = newString.join(" ");
        // console.log("new string", newString)
        console.log("input", string)
        console.log("output", output)
}

spinWords("Hey fellow warriors");