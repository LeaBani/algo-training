// rewrite of the code in Python, this one is faster 

function primesSlice(limit) {
    let isPrime = new Set(Array.from({ length: limit - 1 }, (_, i) => i + 2));

    for (let n = 2; n <= Math.sqrt(limit); n++) {
        if (isPrime.has(n)) {
            for (let i = n * n; i <= limit; i += n) {
                isPrime.delete(i);
            }
        }
    }

    return Array.from(isPrime);
}

function sumOfDivided(lst) {
    const primeOfList = [];

    lst.forEach(element => {
        const primes = primesSlice(Math.abs(element));
        primes.forEach(prime => {
            if (element % prime === 0) {
                primeOfList.push([prime, element]);
            }
        });
    });

    const resArray = sumResult(primeOfList);
    return resArray.sort((a, b) => a[0] - b[0]);
}

function sumResult(lst) {
    const sumsDict = {};

    lst.forEach(pair => {
        const [firstValue, secondValue] = pair;
        sumsDict[firstValue] = (sumsDict[firstValue] || 0) + secondValue;
    });

    return Object.entries(sumsDict).map(([key, value]) => [Number(key), value]);
}

 