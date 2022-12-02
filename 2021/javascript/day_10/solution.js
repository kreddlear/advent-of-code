// parse file into usable strings
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input_test.txt', 'utf8');
const stringData = data.toString();
// split it by newline
const arrayOfLines = stringData.split('\n');

// first instance of term pair char that isn't preceded by a starting pair char

const getCharCount = () => {
    const characterCount = {
        '(': 0,
        '[': 0,
        '{': 0,
        '<': 0
    }
    return characterCount;
}

const openChars = '([{<';

const closeToOpenMap = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

const parseLine = (currentLine) => {
    const currentCharCount = getCharCount();
    const currentList = currentLine.split('');
    let corruptedChar;
    for (const char of currentList) {
        if (openChars.includes(char)) {
            currentCharCount[char] += 1;
        } else {
            currentCharCount[closeToOpenMap[char]] -= 1;
            if (currentCharCount[closeToOpenMap[char]] < 0) {
                corruptedChar = char;
                break;
            }
        }
        console.log(currentCharCount)
    }
    return corruptedChar;
}



const testLine = '{([(<{}[<>[]}>{[]{[(<()>';
// const test = parseLine(testLine);
// console.log(test)

const regex = /\[\]|\(\)|\{\}|\<\>/gm;

const testRegex = testLine.replace(regex, '');
console.log(testRegex);