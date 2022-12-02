// parse file into usable strings
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input.txt', 'utf8');
const stringData = data.toString();
// split it
const contentArray = stringData.split(',');

// convert to ints
for (let a=0; a<contentArray.length; a++) {
    contentArray[a] = parseInt(contentArray[a])
}
console.log(contentArray)

// return the difference
const diffCalculator = (a, b) => {
    const delta = (a > b) ? (a - b) : (b - a);
    return delta;
}

// calculate fuel usage to get to a particular number
const calculateFuel = (numberGoal, array) => {
    let totalFuelUsed = 0;
    for (let a=0; a<array.length; a++) {
        const diffNum = diffCalculator(array[a], numberGoal);
        // okay part 2...I have to get the diff, then iterate over that??
        // 2 to 5: 3 diff, so 1 + 2 + 3 = 6
        // so I should be able to iterate through diff yes
        for (let b=0; b<=diffNum; b++) {
            totalFuelUsed += b;
        }
    }
    return totalFuelUsed;
}

// find the minimum number
const min = Math.min(...contentArray)

// find the maximum number
const max = Math.max(...contentArray);

// num between them?
const average = (max + min)/2

// ok let's just try every number between the min and max
let allFuelTotals = [];
for (let a=min; a<=average; a++) {
    newTotal = calculateFuel(a,contentArray);
    // const miniArray = [a, newTotal]
    // allFuelTotals.push(miniArray);
    allFuelTotals.push(newTotal);
}
console.log(allFuelTotals);
const minBelowAverage = Math.min(...allFuelTotals);

for (let a=average; a<=max; a++) {
    newTotal = calculateFuel(a,contentArray);
    // const miniArray = [a, newTotal]
    // allFuelTotals.push(miniArray);
    allFuelTotals.push(newTotal);
}
console.log(allFuelTotals);
const minAboveAverage = Math.min(...allFuelTotals);

if (minBelowAverage > minAboveAverage) {
    console.log(minBelowAverage);
} else {
    console.log(minAboveAverage);
}