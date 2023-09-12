function encrypt(text, n) {
    const words = text.split('');
    
    const evenIndex = [];
    const oddIndex = [];

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
    
    const newArray = evenIndex.concat(oddIndex)
    console.log(newArray)
    const newLettersArray = [];

    newArray.forEach(element => {
        const findLetter = words[element];
        newLettersArray.push(findLetter)
    });

    const newString = newLettersArray.join('');
    console.log(newString)
}

function decrypt(encryptedText, n) {

}

encrypt("This is a test!", 0)