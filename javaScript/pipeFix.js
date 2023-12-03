function pipeFix(numbers){

    const array = [];
    
    for (const elem of numbers) {
        array.push(elem)
    }

    for (let index = 0; index < numbers.length; index++) {
        const element = numbers[index];
        console.log(element)
        if (element - (numbers[index] -1) === 1) {
            console.log(element, numbers[index])
            if (!numbers.includes(element+1)) {    
                array.push(element+1)
            }
        } else {
            console.log('test')
        }
        
    }


    const sortArray = 
    array.sort(function(a, b) {
        return a - b;
      })

      console.log(sortArray)

    return sortArray;
}

pipeFix([1,2,3,12])