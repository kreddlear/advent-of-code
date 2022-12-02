// parse file into usable strings
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input.txt', 'utf8');
const stringData = data.toString();
// split it by the pipe first
const contentArray = stringData.split('\n');

// split up the pieces
let halfSplitArray = []
for (let a=0; a<contentArray.length; a++) {
    halfSplitArray.push(contentArray[a].split('|'));
}

/*
zero: six
one: two !
two: five
three: five
four: four !
five: five
six: six
seven: three !
eight: seven !
nine: six

one: two
four: four
seven: three
eight: seven
*/

// function to iterate through ten nums and return list of array of nums
const getAllNums = (tenNumsString) => {
    // now get and split up the ten numbers at the beginning
    let tenNumsArray = (tenNumsString.split(' ')).filter(x => x!='')
    // console.log(tenNumsArray);

    let zeroSixOrNineArray = []
    let twoThreeOrFiveArray = []

    let arrayOfZeroSegments = [];
    let arrayOfOneSegments = []
    let arrayOfTwoSegments = [];
    let arrayOfThreeSegments = [];
    let arrayOfFourSegments = []
    let arrayOfFiveSegments = [];
    let arrayOfSixSegments = [];
    let arrayOfSevenSegments = []
    let arrayOfEightSegments = []
    let arrayOfNineSegments = [];

    // get unique numbers
    for (let b=0; b<tenNumsArray.length; b++) {
        // first get unique numbers
        if (tenNumsArray[b].length == 2) {
            arrayOfOneSegments = tenNumsArray[b].split('');
        } else if (tenNumsArray[b].length == 4) {
            arrayOfFourSegments = tenNumsArray[b].split('');
        } else if (tenNumsArray[b].length == 3) {
            arrayOfSevenSegments = tenNumsArray[b].split('');
        } else if (tenNumsArray[b].length == 7) {
            arrayOfEightSegments = tenNumsArray[b].split('');
        } else if (tenNumsArray[b].length == 6) {
            zeroSixOrNineArray.push(tenNumsArray[b])
        } else if (tenNumsArray[b].length == 5) {
            twoThreeOrFiveArray.push(tenNumsArray[b]);
        }
    }

    // list of all segment variables
    let segmentObject = {
        segmentTopChar: '',
        segmentMiddleChar: '',
        segmentBottomChar: '',

        segmentUpperRightChar: '',
        segmentLowerRightChar: '',

        segmentUpperLeftChar: '',
        segmentLowerLeftChar: '',
    }

    // 1 and 7 share the upper and lower right segments, the segment not part of 1 is the top char
    for (let a=0; a<arrayOfSevenSegments.length; a++) {
        let charToCheck = arrayOfSevenSegments[a];
        let doesOneIncludeIt = arrayOfOneSegments.includes(charToCheck);
        if (doesOneIncludeIt == false) {
            segmentObject.segmentTopChar = arrayOfSevenSegments[a];
        }
    }

    // let's make this countincommon thing into a function.
    const countSegmentsInCommon = (string, array) => {
        let stringArray = string.split('');
        let countInCommon = 0;
        for (let c=0; c<stringArray.length; c++) {
            let charToCheck = stringArray[c]
            if (array.includes(charToCheck)) {
                countInCommon++;
            }
        }
        return countInCommon;
    }

    // zero, six, and nine all have six segments
    // I think I can work with six...it shares the top (which I know) and the lower right with seven
    // so I can compare them and know what the upper right is because that's the one that's not in six
    // if the char matches the segmentTopChar, ignore it
    // iterate through each string in the zeroSixOrNineArray
    for (let b=0; b<zeroSixOrNineArray.length; b++) {
        let stringToCheck = zeroSixOrNineArray[b]
        // now iterate through each char in each string
        // count how many are present in the seven list of segments
        let countInCommon = countSegmentsInCommon(stringToCheck, arrayOfSevenSegments);
        // count how many chars it shares with seven
        // if that count is 2, that's six -- split that up and set it to the arrayOfSixSegments
        if (countInCommon == 2) {
            arrayOfSixSegments = stringToCheck.split('');
        }
    }

    // and then now that I know which one is six, I should be able to figure out the upper right one...how?
    // one's segments are both on the right
    // the segment in one that is not in six is the upper right
    // console.log(arrayOfOneSegments);
    for (let d=0; d<arrayOfOneSegments.length; d++) {
        if (arrayOfSixSegments.includes(arrayOfOneSegments[d]) == false) {
            segmentObject.segmentUpperRightChar = arrayOfOneSegments[d];
        } else {
            segmentObject.segmentLowerRightChar = arrayOfOneSegments[d];
        }
    }

    // okay now that I have six and I know one and seven,
    // can I figure out which one is nine vs zero?
    // yes -- I know 4, and I know zero has 3 segments in common with 4
    // whereas 9 has 4 segments in common with 4
    // console.log(zeroSixOrNineArray);
    for (let a=0; a<zeroSixOrNineArray.length; a++) {
        // if it's not 6...
        if (zeroSixOrNineArray[a] != arrayOfSixSegments.join('')) {
            let countInCommon = countSegmentsInCommon(zeroSixOrNineArray[a], arrayOfFourSegments)
            // if they have 3 in common, set that split string equal to zero
            if (countInCommon == 3) {
                arrayOfZeroSegments = zeroSixOrNineArray[a].split('');
            } else {
                // and the other equal to nine
                arrayOfNineSegments = zeroSixOrNineArray[a].split('');
            }
        }
    }

    // okay so now let's compare six and zero to find out the middle
    for (let a=0; a<arrayOfSixSegments.length; a++) {
        // if we find a char that is not in zero but is in six
        // AND that char is not the upper right char
        if (!arrayOfZeroSegments.includes(arrayOfSixSegments[a]) && arrayOfSixSegments[a] != segmentObject.segmentUpperRightChar) {
            // dammit something is going wrong here because two of the segments are the smae and i don't know why!!  d
            segmentObject.segmentMiddleChar = arrayOfSixSegments[a];
        }
    }

    // now go through 4 -- the one we don't know is upper left
    let onesWeKnow = Object.values(segmentObject);
    for (let a=0; a<arrayOfFourSegments.length; a++) {
        if (!onesWeKnow.includes(arrayOfFourSegments[a])) {
            segmentObject.segmentUpperLeftChar = arrayOfFourSegments[a];
        }
    }

    // now go through 2, 3 and 5
    for (let a=0; a<twoThreeOrFiveArray.length; a++) {
        let stringToCheck = twoThreeOrFiveArray[a];
        let countInCommon = countSegmentsInCommon(stringToCheck, arrayOfSevenSegments);
        // if the number has 3 in common with seven, it's three
        if (countInCommon == 3) {
            arrayOfThreeSegments = twoThreeOrFiveArray[a].split('')
        } 
    }

    // use three to figure out the bottom segment
    let onesWeKnowNow = Object.values(segmentObject);
    for (let a=0; a<arrayOfThreeSegments.length; a++) {
        if (!onesWeKnowNow.includes(arrayOfThreeSegments[a])) {
            segmentObject.segmentBottomChar = arrayOfThreeSegments[a];
        }
    }

    // use three to figure out the lower left segment
    let onesWeKnowNowNow = Object.values(segmentObject);
    for (let a=0; a<arrayOfZeroSegments.length; a++) {
        if (!onesWeKnowNowNow.includes(arrayOfZeroSegments[a])) {
            segmentObject.segmentLowerLeftChar = arrayOfZeroSegments[a];
        }
    }

    // use the lower left segment to figure out if it's two or five
    for (let a=0; a<twoThreeOrFiveArray.length; a++) {
        let arrayToCheck = twoThreeOrFiveArray[a].split('');
        if (arrayToCheck.includes(segmentObject.segmentLowerLeftChar)) {
            arrayOfTwoSegments = arrayToCheck;
        } else if (arrayToCheck.includes(segmentObject.segmentUpperLeftChar)) {
            arrayOfFiveSegments = arrayToCheck
        }
    }

    // okay store all the arrays of numbers in an object for easier reference
    let numberArraysObject = {}
    numberArraysObject['0'] = arrayOfZeroSegments.sort();
    numberArraysObject['1'] = arrayOfOneSegments.sort();
    numberArraysObject['2'] = arrayOfTwoSegments.sort();
    numberArraysObject['3'] = arrayOfThreeSegments.sort();
    numberArraysObject['4'] = arrayOfFourSegments.sort();
    numberArraysObject['5'] = arrayOfFiveSegments.sort();
    numberArraysObject['6'] = arrayOfSixSegments.sort();
    numberArraysObject['7'] = arrayOfSevenSegments.sort();
    numberArraysObject['8'] = arrayOfEightSegments.sort();
    numberArraysObject['9'] = arrayOfNineSegments.sort();

    return numberArraysObject;
}

// function to use that list of array of nums to get 4 numbers
const getFourNums = (fourNumsString, objectOfNums) => {
    let fourNumsArray = (fourNumsString.split(' ')).filter(x => x!='')

    const arrayOfNumArrays = Object.values(objectOfNums)

    // make a function to check a number
    const checkThisString = (stringToCheck) => {

        // okay I know I need to split up the string into an array
        let arrayToCheck = stringToCheck.split('').sort();

        // so I have that array that I want to find out what number it is
        // and now I shoud get each number
        for (let z=0; z<arrayOfNumArrays.length; z++) {
            let numArrayToCompare = arrayOfNumArrays[z];

            // for each number, I want to make sure:
            // the length is the same as the array I have
            if (arrayToCheck.length == numArrayToCompare.length) {

                let matchSoFar = true;
                let b=0;
                do {
                    if (arrayToCheck[b] == numArrayToCompare[b]) {
                        // keep checking by incrementing b
                        b++;
                        // also keep checking by setting matchsofar to true
                    } else {
                        // stop checking by setting matchsofar to false
                        matchSoFar = false;
                    }
                } while (matchSoFar == true && b < arrayToCheck.length);

                // okay...so it will exit the loop either way. how do I tell if it was a match?
                if (matchSoFar == true) {
                    return z;
                }
            }
        }
    }

    let stringOfFourNums = '';
    // iterate over the four numbers
    for (let a=0; a<fourNumsArray.length; a++) {
        let stringToCheck = fourNumsArray[a];
        // use the above function to find out which number it is
        stringOfFourNums += checkThisString(stringToCheck);
    }
    return stringOfFourNums;

}

let sumTotal = 0;
for (let d=0; d<halfSplitArray.length; d++) {
    const whatAreNums = getAllNums(halfSplitArray[d][0]);
    const theseFourNums = getFourNums(halfSplitArray[d][1], whatAreNums);
    sumTotal += parseInt(theseFourNums);
}

console.log(sumTotal)

/*

const reducer = (previousValue, currentValue) => previousValue + currentValue;

const countsArray = Object.values(numsCountObject);
console.log(countsArray.reduce(reducer));

// reminder: REMOVE FIRST LINE OF TEST INPUT BEFORE TRYING
*/