// read file
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input.txt', 'utf8');
const stringData = data.toString();
// split it by newline
const binaryNumsArray = stringData.split('\n');

// let's write a function that returns the most or least common num at that bit position
const getMostOrLeastCommonCharAtN = (array, desiredIndex, gammaOrEpsilon) => {
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
    
    // more common
    if (gammaOrEpsilon == 'gamma') {
        if (zeroCounter > oneCounter) {
            return 0;
        } else if (zeroCounter < oneCounter) {
            return 1;
        } else {
            return 1;
        }
    } else if (gammaOrEpsilon == 'epsilon') {
        // less common
        if (zeroCounter > oneCounter) {
            return 1;
        } else if (zeroCounter < oneCounter) {
            return 0;
        } else {
            return 0;
        }
    }
};

// function that only includes numbers with mostCommon at that particular index
const onlyIncludeValidItems = (array, desiredIndex, numToCheck) => {
    const newArray = array.filter(item => item[desiredIndex] == numToCheck);
    return newArray;
}

const wittleDownArray = (array, gammaOrEps) => {

    let constantlyChangingArray = array;

    // go through each binary number but only for the amount of chars it has
    for (let i=0; i < array[0].length; i++) {
        console.log(constantlyChangingArray);

        if (constantlyChangingArray.length > 1) {
            // get the most common bit at that index
            const mostOrLeastCommon = getMostOrLeastCommonCharAtN(constantlyChangingArray, i, gammaOrEps);
            console.log("mostOrLeastCommon for ", i, "is: ", mostOrLeastCommon);

            const resultArray = onlyIncludeValidItems(constantlyChangingArray, i, mostOrLeastCommon);

            constantlyChangingArray = resultArray;
            console.log(constantlyChangingArray);
        } else {
            console.log(constantlyChangingArray);
        }
    }

    return constantlyChangingArray;

}

const finalBinaryOxy = wittleDownArray(binaryNumsArray, 'gamma');
const finalBinaryC02 = wittleDownArray(binaryNumsArray, 'epsilon');

// parseInt with base 2
const gamma = parseInt(finalBinaryOxy, 2);
const epsilon = parseInt(finalBinaryC02, 2);

console.log("multiplier: ", gamma * epsilon);