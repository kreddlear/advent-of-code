// parse file into usable strings
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input.txt', 'utf8');
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

// function that will be recursive -- calls itself within itself
const exploreChunk = (fullHeightmap, rowNum, columnNum, currentChunkCount, listOfAllCoordsInAnyChunks) => {
    // console.log("current chunk count at the very beginning: ", currentChunkCount);
    // checks if the point has not been seen before (so it isn't in multiple chunks)
    if (!listOfAllCoordsInAnyChunks.includes(`x${rowNum}y${columnNum}`)) {

        // checks if the point value is not 9
        if (fullHeightmap[rowNum][columnNum] && fullHeightmap[rowNum][columnNum] != 9) {
            // push that point's coords to list of nums in current chunk??
            // (in case we need to keep using it...maybe??)
            // maybe we don't care about that though

            // console.log(`now parsing x${rowNum}y${columnNum}`);
            
            // +1 to count of nums in chunk
            currentChunkCount += 1;
            // console.log("current chunk count: ", currentChunkCount);

            // +1 that point's coords to coordinates in ANY chunk
            listOfAllCoordsInAnyChunks.push(`x${rowNum}y${columnNum}`);
            // console.log("list of all coords in chunks: ", listOfAllCoordsInAnyChunks);

            // go get its adjacents
            // wait what do we care about w.r.t the adjacents?
            // yes their value because if they are a 9 we don't care
            // but also their coords, right? because we need the row num and column num
            const newAdjacents = returnAdjacent(fullHeightmap, rowNum, columnNum);
            // console.log("new adjacents: ", newAdjacents);

            // then do this all again for each adjacent that is not zero
            for (const direction in newAdjacents) {
                // console.log("now in the for loop, direction is ", direction)
                if (direction == 'north') {
                    currentChunkCount = exploreChunk(fullHeightmap, rowNum-1, columnNum, currentChunkCount, listOfAllCoordsInAnyChunks)
                } else if (direction == 'east') {
                    // dammit, wait, I want the current chunk count to keep increasing!
                    // how do I not reset it every time??
                    currentChunkCount = exploreChunk(fullHeightmap, rowNum, columnNum+1, currentChunkCount, listOfAllCoordsInAnyChunks)
                } else if (direction == 'south') {
                    currentChunkCount = exploreChunk(fullHeightmap, rowNum+1, columnNum, currentChunkCount, listOfAllCoordsInAnyChunks)
                } else if (direction == 'west') {
                    currentChunkCount = exploreChunk(fullHeightmap, rowNum, columnNum-1, currentChunkCount, listOfAllCoordsInAnyChunks)
                }
            }
            return currentChunkCount;
        } else {
            // console.log("either doesn't exist or is 9!")
            return currentChunkCount;
        }
    } else {
        // console.log("already seen it!!");
        return currentChunkCount;
    }
}

// need to do something with this var while iterating
let alreadyInChunks = [];
let arrayOfBasins = [];

// iterate over every row in the array
for (let a=0; a<arrayOfNums.length; a++) {
    // iterate over every column in the row
    for (let b=0; b<arrayOfNums[a].length; b++) {
        const point = arrayOfNums[a][b]
        const adjacents = returnAdjacent(arrayOfNums, a, b)
        if (checkIfLowPoint(point, adjacents)) {
            let currentBasinSize = exploreChunk(arrayOfNums, a, b, 0, alreadyInChunks);
            // console.log(`low point: x${a}y${b} count equals ${currentBasinSize}`);
            arrayOfBasins.push(currentBasinSize);
        }
    }
}
console.log(arrayOfBasins);

// now find the largest basin
let largestBasins = [];
const biggest = Math.max(...arrayOfBasins);
largestBasins.push(biggest);
// now set that index to zero so it can't be the max again
// and also so if there's more than one it will still be there
arrayOfBasins[arrayOfBasins.indexOf(biggest)] = 0;

const nextBiggest = Math.max(...arrayOfBasins);
largestBasins.push(nextBiggest);
arrayOfBasins[arrayOfBasins.indexOf(nextBiggest)] = 0;

const thirdBiggest = Math.max(...arrayOfBasins);
largestBasins.push(thirdBiggest);

console.log(largestBasins);

// and multiply them together

const reducer = (previousValue, currentValue) => previousValue * currentValue;
console.log(largestBasins.reduce(reducer));

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
