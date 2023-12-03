function generateHashtag (str) {

    
    const strWithoutSpace = str.replaceAll(" ", "")
    const strLength = strWithoutSpace.length;

    if (strLength > 139 || strWithoutSpace === "") {
        console.log(false)
        return false;

    } else {
        const array = []
    
        const words = str.split(' ');

        words.forEach(word => {
            const wordToUpperCase = word.charAt(0).toUpperCase() + word.slice(1);
            array.push(wordToUpperCase);
        });    
    
        // console.log(array)
    
        const newString = array.join("");    
        // console.log(str2)
    
        const hashtag = "#";
        const hashtagString = hashtag.concat(newString);
    
        console.log(hashtagString)

        return hashtagString;
        
    }
}

generateHashtag("code" + " ".repeat(140) + "wars")