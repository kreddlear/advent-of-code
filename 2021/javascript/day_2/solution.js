// read file
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input.txt', 'utf8');
const stringData = data.toString();
// split it by newline
// this should output an array like ['forward 5', 'down 3']
const newlineArray = stringData.split('\n');

// function to take a text and number and output each as the proper type
const parsePositionInstruction = (input) => {
    const inputSplitArray = input.split(" ");
    const direction = inputSplitArray[0];
    const amount = parseInt(inputSplitArray[1]);
    return {
        direction: direction,
        amount: amount
    };
};

let horizontalPosition = 0;
let depth = 0;
// part 2
let aim = 0;

// loop over array of instructions
for (let i=0; i < newlineArray.length; i++) {
    const something = parsePositionInstruction(newlineArray[i]);

    switch (something.direction) {
        case 'down':
            // update aim - add
            aim += something.amount;
            console.log("aim: ", aim);
            break;
        case 'up':
            // update aim - subtract
            aim -= something.amount;
            console.log("aim: ", aim);
            break;
        case 'forward':
            // update horizontal position - add X
            // update depth - aim * X
            horizontalPosition += something.amount;
            depth += aim * something.amount
            console.log("horizontalPosition: ", horizontalPosition)
            console.log("depth: ", depth);
            break;
    }
}

console.log("horizontalPosition: ", horizontalPosition, " depth: ", depth, " total: ", horizontalPosition * depth);