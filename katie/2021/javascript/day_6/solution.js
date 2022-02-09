// parse file into usable strings
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input.txt', 'utf8');
const stringData = data.toString();
// split it by newline
const contentArray = stringData.split(',');
console.log(contentArray);

/*
So, suppose you have a lanternfish with an internal timer value of 3:

After one day, its internal timer would become 2.
After another day, its internal timer would become 1.
After another day, its internal timer would become 0.
After another day, its internal timer would reset to 6, 
and it would create a new lanternfish with an internal timer of 8.
After another day, the first lanternfish would have an internal timer of 5, 
and the second lanternfish would have an internal timer of 7.

*/

// keep track of how many fishes of each type there are
let fishTracker = {
    fish8: 0,
    fish7: 0,
    fish6: 0,
    fish5: 0,
    fish4: 0,
    fish3: 0,
    fish2: 0,
    fish1: 0,
    fish0: 0,
}

// iterate over initial list and add counts to fishTracker
for (let a=0; a<contentArray.length; a++) {
    contentArray[a] = parseInt(contentArray[a])
    fishTracker[`fish${contentArray[a]}`] += 1
}
console.log(fishTracker);

// function to, every day, iterate through fishTracker and update every timer count 
// to the LOWER timer's count
const dayCycle = (fishCountObject) => {

    let newFishObject = {}

    // create new fish!
    // take the zero count (fish that are resetting aka creating new fish)
    // and set the 8 count to that
    newFishObject.fish8 = fishCountObject.fish0;

    // for testing, just set fish8 to 0 for now
    // newFishObject['fish8'] = 0;

    for (let b=7; b>=0; b--) {
        // console.log(fishCountObject[`fish${b}`])
        // newFishObject.fish7 = fishCountObject.fish8
        // newFishObject.fish6 = fishCountObject.fish7
        // newFishObject.fish5 = fishCountObject.fish6
        // newFishObject.fish4 = fishCountObject.fish5
        // newFishObject.fish3 = fishCountObject.fish4
        // newFishObject.fish2 = fishCountObject.fish3
        // newFishObject.fish1 = fishCountObject.fish2
        // newFishObject.fish0 = fishCountObject.fish1
        // console.log(`take newFishObject['fish${b}'] and set it to fishCountObject['fish${b+1}']`);
        newFishObject[`fish${b}`] = fishCountObject[`fish${[b+1]}`]

    }

    // reset the fish!
    // take the zero count and add it to the existing count of 6
    newFishObject.fish6 = newFishObject.fish6 + fishCountObject.fish0

    fishTracker = newFishObject;

};

/*
// 1 day
dayCycle(fishTracker);
console.log(fishTracker);
// 2 days
dayCycle(fishTracker);
console.log(fishTracker);
*/

// function to iterate through each day
const dayCount = 256;

for (let a=0; a<dayCount; a++) {
    dayCycle(fishTracker);
}

console.log(fishTracker);

// ANSWER: sum all counts
const reducer = (previousValue, currentValue) => previousValue + currentValue;

const fishCountsArray = Object.values(fishTracker);
console.log(fishCountsArray.reduce(reducer));

// I DID IT!!!!!!!!!!!!!!!!!!!