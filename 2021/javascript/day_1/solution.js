// read file

const fs = require('fs');

// get it into an array that's possible to split
const data = fs.readFileSync('./input.txt', 'utf8');
const stringData = data.toString();
const stringArrayData = stringData.split('\n');
const arrayData = stringArrayData.map(x => parseInt(x));

// count the number of times a depth measurement increases from the previous measurement

// set numberIncreases to 0
let numIncreases = 0;

// loop through array of input
// wait are they strings or numbers because that might cause some issues...YEP it sure did

for (let i=0; i < arrayData.length; i++) {
    // store current array index
    let currentIndex = arrayData[i];
    
    // store followup index
    let nextIndex = arrayData[i+1];
    
    // part 2
    let thirdIndex = arrayData[i+2];

    // sum those
    let firstWindow = currentIndex + nextIndex + thirdIndex;
    console.log("firstWindow", firstWindow);

    // store fourth index for next window
    let fourthIndex = arrayData[i+3];
    
    // sum next, third, and fourth indexes
    let secondWindow = nextIndex + thirdIndex + fourthIndex;
    console.log("secondWindow", secondWindow);

    // compare the two windows
    if (secondWindow > firstWindow) {
        numIncreases++;
    }
}
console.log(numIncreases);