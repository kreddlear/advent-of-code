// read file
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input.txt', 'utf8');
const stringData = data.toString();
// split it by newline
const binaryNumsArray = stringData.split('\n');

// how do I parse binary in JS?

// get the nth character in the item of the array

// zeroCounter
// oneCounter

/*
// checking if all the strings are the same length...looks fine
for (let i=0; i < binaryNumsArray.length; i++) {
    const firstNumLength = binaryNumsArray[0].length;
    if (binaryNumsArray[i].length != firstNumLength) {
        throw new Error("OMG WATCH OUT FOR INDEX ", i);
    }
}
*/

// let's write a function
const getNthCharCounts = (array, desiredIndex, gammaOrEpsilon) => {
    console.log("now running for index ", desiredIndex);
    // do they all have the same number of indices?

    let zeroCounter = 0;
    let oneCounter = 0;

    // iterate through array
    for (let j=0; j<array.length; j++) {
        if (array[j][desiredIndex] == 0) {
            zeroCounter++;
        } else if (array[j][desiredIndex] == 1) {
            oneCounter++;
        }
    }
    
    if (gammaOrEpsilon == 'gamma') {
        if (zeroCounter > oneCounter) {
            return 0;
        } else if (zeroCounter < oneCounter) {
            return 1;
        } else {
            throw new Error("equal?!?");
        }
    } else if (gammaOrEpsilon == 'epsilon') {
        if (zeroCounter > oneCounter) {
            return 1;
        } else if (zeroCounter < oneCounter) {
            return 0;
        } else {
            throw new Error("equal?!?");
        }
    }
};

let finalGammaBinaryNumArray = [];

// go through each binary number but only for the amount of chars it has
for (let i=0; i < binaryNumsArray[0].length; i++) {
    finalGammaBinaryNumArray.push(getNthCharCounts(binaryNumsArray, i, 'gamma'));
}

let finalEpsilonBinaryNumArray = [];

// go through each binary number but only for the amount of chars it has
for (let i=0; i < binaryNumsArray[0].length; i++) {
    finalEpsilonBinaryNumArray.push(getNthCharCounts(binaryNumsArray, i, 'epsilon'));
}

console.log("gamma: ", finalGammaBinaryNumArray);
console.log("epsilon: ", finalEpsilonBinaryNumArray);
let finalGammaBinaryNum = finalGammaBinaryNumArray.join('');
let finalEpsilonBinaryNum = finalEpsilonBinaryNumArray.join('');

// parseInt with base 2
const gamma = parseInt(finalGammaBinaryNum, 2);
const epsilon = parseInt(finalEpsilonBinaryNum, 2);

console.log("multiplier: ", gamma * epsilon);