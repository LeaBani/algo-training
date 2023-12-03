function encrypt(text, n) {
    

    const words = text.split('');
    
    let evenIndex = [];
    let oddIndex = [];
    
        // ici, je genère mes index pairs et impairs

            words.forEach(word => {
                const indexOfString = [];
                const indexOfWord = words.indexOf(word);
                // console.log(indexOfWord)
                indexOfString.push(indexOfWord)
        
                for (const i of indexOfString) {
                    if (i % 2 === 0) {
                        evenIndex.push(i)
                    } else {
                        oddIndex.push(i)
                    }
                }
        
            });
            
        // ici, je concatene mes 2 tableau d'index


    const newArray = oddIndex.concat(evenIndex)
    console.log('array of index', newArray)

    for (let index = 0; index < n; index++) {
        newArray.forEach(element => {
            const indexOfString = [];
                const indexOfWord = newArray.indexOf(element);
                // console.log(indexOfWord)
                indexOfString.push(indexOfWord)
        
                for (const i of indexOfString) {
                    if (i % 2 === 0) {
                        evenIndex.push(i)
                    } else {
                        oddIndex.push(i)
                    }
                }
                // ici, je reconstitue la chaine de char
            const newLettersArray = [];
            newArray.forEach(element => {
                const findLetter = words[element];
                newLettersArray.push(findLetter)
            });
            
            const newString = newLettersArray.join('');
            console.log('new string', newString)
        });
        
    }

}

function decrypt(encryptedText, n) {

}

encrypt("This is a test!", 2)