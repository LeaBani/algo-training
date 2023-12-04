function orderWeight(str) {
    const newDigits = []

    // array of number
    const numbers = str.split(' ')
    // console.log(numbers);
    
    numbers.forEach(element => {
        // console.log(element)
        const sum = element.split('').reduce((sum, digit) => sum + parseInt(digit), 0);
        newDigits.push(sum)
    })
    
    console.log(newDigits);
    numbers.sort((a, b) => {
        // console.log(numbers);
    })
}
  
  const input = "56 65 74 100 99 68 86 180 90";
  const result = orderWeight(input);
  console.log(result); // Output: "100 180 90 56 65 74 68 86 99"
  