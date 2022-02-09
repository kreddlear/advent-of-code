// parse file into usable strings
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input.txt', 'utf8');
const stringData = data.toString();
// split it by newline
const contentArray = stringData.split('\n');

// parse coordinates from strings into usable pairs
let coordinatesStringsArray = [];
for (let a=0; a<contentArray.length; a++) {
    // split into usable string pairs
    const coordPairArray = contentArray[a].split(" -> ");
    const coordPairStrings = coordPairArray.map(item => item.split(','))
    coordinatesStringsArray.push(coordPairStrings);
}

// parse array of coordinate strings into...array of labeled coordinate objects?
let coordinateObjectArray = [];
for (let b=0; b<coordinatesStringsArray.length;b++) {
    let newObject = {};
    newObject.x1 = parseInt(coordinatesStringsArray[b][0][0])
    newObject.y1 = parseInt(coordinatesStringsArray[b][0][1])
    newObject.x2 = parseInt(coordinatesStringsArray[b][1][0])
    newObject.y2 = parseInt(coordinatesStringsArray[b][1][1])
    coordinateObjectArray.push(newObject);
}
// console.log(coordinateObjectArray);

const diff = (a, b) => {
    const delta = (a > b) ? (a - b) : (b - a);
    let larger = Math.max(a,b);
    let smaller = Math.min(a,b);
    return {
        delta,
        larger,
        smaller,
    }
}

// need to get a list of coordinates between two coordinates given
const generateAllBetweenCoordinates = (coordinateObject) => {
    const {x1,y1,x2,y2} = coordinateObject;
    // console.log(`now processing: x${x1}y${y1} and x${x2}y${y2}`)

    // this will be a list of keys
    let listOfCoordinates = [];

    // first check if it's vertical or horizontal
    if (x1 == x2) {
        // vertical - get all numbers between y1 and y2
        // ex 7,0 > 7,4
        let deltaInfo = diff(y1,y2);
        for (let c=0; c < deltaInfo.delta + 1; c++) {
            const key = `x${x1}y${deltaInfo.smaller+c}`;
            listOfCoordinates.push(key);
        }
    } else if (y1 == y2) {
        // horizontal - get all numbers between x1 and x2
        let deltaInfo = diff(x1,x2);
        for (let c=0; c < deltaInfo.delta + 1; c++) {
            const key = `x${deltaInfo.smaller + c}y${y1}`;
            listOfCoordinates.push(key);
        }
    } else {
        // diagonal
        console.log(`diagonal keys detected: x${x1}y${y1} and x${x2}y${y2}`)

        // generate list of X keys
        let deltaXInfo = diff(x1,x2);
        let xKeysList = [];
        // if x2 is larger, add to x1 to get there
        if (x1 == deltaXInfo.smaller) {
            for (let c=0; c < deltaXInfo.delta + 1; c++) {
                const xKey = x1+c;
                xKeysList.push(xKey);
            }
        } else if (x2 == deltaXInfo.smaller) {
            // if x2 is smaller, subtract from x1 to get there
            for (let c=0; c < deltaXInfo.delta + 1; c++) {
                const xKey = x1-c;
                xKeysList.push(xKey);
            }
        }
        
        // generate list of Y keys
        let deltaYInfo = diff(y1,y2);
        let yKeysList = [];
        // if y2 is larger, add to y1 to get there
        if (y1 == deltaYInfo.smaller) {
            for (let c=0; c < deltaYInfo.delta + 1; c++) {
                const yKey = y1+c;
                yKeysList.push(yKey);
            }
            console.log("yKeysList: ", yKeysList);
        } else if (y2 == deltaYInfo.smaller) {
            // if x2 is smaller, subtract from x1 to get there
            for (let c=0; c < deltaYInfo.delta + 1; c++) {
                const yKey = y1-c;
                yKeysList.push(yKey);
            }
        }

        // for loop to put them together
        // they should be the same length because 45 degrees
        for (let d=0; d<xKeysList.length; d++) {
            const key = `x${xKeysList[d]}y${yKeysList[d]}`;
            listOfCoordinates.push(key);
        }
    }
    console.log(listOfCoordinates);
    return listOfCoordinates;
}

/*
const testObject = { x1: 8, y1: 0, x2: 0, y2: 8 };
const testObject2 = { x1: 5, y1: 5, x2: 8, y2: 2 };
generateAllBetweenCoordinates(testObject2);
*/

// then check if each coordinate is in an object storing coordinates with corresponding amounts
// if it is, add 1 to that amount
// if it's not, add the coordinate to the list with 1 as an amount
let fullObjectOfCoords = {}
const checkAndLogCoordinates = (coordList) => {
    for (let d=0; d < coordList.length; d++) {
        const coordKey = coordList[d]
        if (fullObjectOfCoords[coordKey]) {
            fullObjectOfCoords[coordKey] += 1;
        } else {
            fullObjectOfCoords[coordKey] = 1;
        }
    }
}

for (let e=0; e<coordinateObjectArray.length; e++) {
    const listOfCoords = generateAllBetweenCoordinates(coordinateObjectArray[e]);
    checkAndLogCoordinates(listOfCoords);
}

// console.log(fullObjectOfCoords);

// finally, count how many coordinates in the list have more than 1 as an amount
const valuesArray = Object.values(fullObjectOfCoords);
console.log(valuesArray);
const filteredValuesArray = valuesArray.filter(item => item > 1)
console.log(filteredValuesArray);
console.log(filteredValuesArray.length)