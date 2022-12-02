// parse file into usable strings
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input_test.txt', 'utf8');
const stringData = data.toString();
// split it by newline
const contentArray = stringData.split('\n');
let arrayOfNums = [];
contentArray.forEach(x => arrayOfNums.push(x.split('')))

const returnAdjacent = (fullHeightmap, rowNum, columnNum) => {
    let adjacentObject = {};
    // north
    if (fullHeightmap[rowNum-1]) {
        adjacentObject.north = parseInt(fullHeightmap[rowNum-1][columnNum])
    }
    // east
    if (fullHeightmap[rowNum][columnNum+1]) {
        adjacentObject.east = parseInt(fullHeightmap[rowNum][columnNum+1])
    }
    // south
    if (fullHeightmap[rowNum+1]) {
        adjacentObject.south = parseInt(fullHeightmap[rowNum+1][columnNum])
    }
    // west
    if (fullHeightmap[rowNum][columnNum-1]) {
        adjacentObject.west = parseInt(fullHeightmap[rowNum][columnNum-1])
    }
    return adjacentObject;
}

const checkIfLowPoint = (currentPoint, currentAdjacentObject) => {
    // turn adjacents into array to make it easier
    let arrayToTest = Object.values(currentAdjacentObject)
    // add the test point to that
    arrayToTest.push(parseInt(currentPoint));

    // find minimum
    const min = Math.min(...arrayToTest);
    // Math.min returns the minimum even if numbers are equal
    // we only want it if it's actually the lowest
    const existsMoreThanOnce = arrayToTest.filter(x => x == min)
    if (existsMoreThanOnce.length > 1) {
        return false;
    }
    // now see if it's a low point
    // if testPoint == minimum of itself and adjacents
    if (min == currentPoint) {
        return true;
    } else {
        return false;
    }
}

let arrayOfLowPoints = [];
// iterate over every row in the array
for (let a=0; a<arrayOfNums.length; a++) {
    // iterate over every column in the row
    for (let b=0; b<arrayOfNums[a].length; b++) {
        const point = arrayOfNums[a][b]
        const adjacents = returnAdjacent(arrayOfNums, a, b)
        if (checkIfLowPoint(point, adjacents)) {
            arrayOfLowPoints.push(parseInt(point));
        }
    }
}
console.log(arrayOfLowPoints);

// add up risk points
let arrayOfRiskPoints = [];
arrayOfLowPoints.forEach(x => arrayOfRiskPoints.push(x+1))

const reducer = (previousValue, currentValue) => previousValue + currentValue;
console.log(arrayOfRiskPoints.reduce(reducer));

// low points - the locations that are lower than any of its adjacent locations
// Most locations have four adjacent locations (up, down, left, and right)
// locations on the edge or corner of the map have three or two adjacent locations, respectively
// diagonals don't count

// answers to input test:
// 1 and 0 in row 1
// 5 in row 3
// 5 in row 5

// risk level of a low point is 1 plus its height. row doesn't matter!!!
// In the above example, the risk levels of the low points are 2, 1, 6, and 6 because:
// (1 + 1) and (1 + 0)
// 1 + 5
// 1 + 5

// The answer is the sum of the risk levels of all low points
// so the answer to the test is 15

// 9 is always going to be higher
// 0 is always going to be lower than everything

