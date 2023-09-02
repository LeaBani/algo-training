function findOutlier(integers){
    //your code here

    const oddNumbers = [];
    const evenNumbers = [];

    for (const elem of integers) {
        if (elem % 2 === 0) {
            evenNumbers.push(elem)
        } else {
            oddNumbers.push(elem)
        }
    }

    console.log(oddNumbers, evenNumbers)
    
    if (evenNumbers.length === 1) {
        console.log(evenNumbers.find(elem => elem))
        console.log(Number(evenNumbers.join()))
        return evenNumbers.find(elem => elem);
    } else {
        console.log(oddNumbers.find(elem => elem))
        return oddNumbers.find(elem => elem);
    }

  }

findOutlier([1,1,0,1,1])