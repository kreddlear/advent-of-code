// read file
const { table } = require('console');
const fs = require('fs');

// get it into an array
const data = fs.readFileSync('./input.txt', 'utf8');
const stringData = data.toString();
// split it by newline
const contentArray = stringData.split('\n\n');
// console.log(contentArray);

// Parse First Line
const calledNumsString = contentArray[0];
// parse the first line into usable numbers
calledNumsArray = calledNumsString.split(',');
console.log(calledNumsArray);

let fullTablesArray = [];

// Parse Tables
// iterate through rest of array
for (let i=1; i < contentArray.length; i++) {
    const lineArray = contentArray[i].split('\n');
    // console.log("lineArray: ", lineArray);

    let newTableArray = [];

    for (let k=0; k < lineArray.length; k++) {
        const numArray = lineArray[k].split(' ');
        const filteredArray = numArray.filter(item => item != '')
        // console.log(filteredArray);
        newTableArray.push(filteredArray);
    }

    // console.log("newTableArray", newTableArray);

    // now put it all back together in a giant array
    fullTablesArray.push(newTableArray);
}

// returns true if bingo in specified row
const checkRowForBingo = (rowArray) => {
    let columnIndex=0;
    do {
        // console.log("now checking ", columnIndex)
        if (rowArray[columnIndex] == 'XX') {
            columnIndex++;
        } else {
            // if a row doesn't have bingo, immediately fail
            return false;
        }
    } while (columnIndex < 5);

    return true;
}

// returns true if bingo in specified column
const checkColumnForBingo = (tableArray, columnIndex) => {
    let rowNumber=0;
    do {
        // console.log("now checking row ", rowNumber)
        if (tableArray[rowNumber][columnIndex] == 'XX') {
            rowNumber++;
        } else {
            // if a column doesn't have bingo, immediately fail
            return false;
        }
    } while (rowNumber < 5);

    return true;
}

// returns true if bingo in either a row or column
const checkTableForBingo = (tableArray, rowNumber, columnIndex) => {
    // check specified row
    const isRowBingo = checkRowForBingo(tableArray[rowNumber])
    if (isRowBingo) {
        // if row is bingo, immediately true
        return true;
    } else {
        // if row is not bingo, check specified column
        const isColumnBingo = checkColumnForBingo(tableArray, columnIndex)
        if (isColumnBingo) {
            // if column is bingo, immediately true
            return true;
        } else {
            // else fail
            return false;
        }
    }
}

// if number not found, return false
// if number found, return a new array with XX in the number's place
const checkTableForNumber = (tableArray, calledNumber) => {
    let rowNumber = 0;
    let columnNumber = 0;

    // I can use a do/while because the number will only occur once in a table
    // so as soon as foundNumber is true, we want to set that number to XX
    // then stop looking and return True

    // check every row
    do {
        // console.log("checking row number: ", rowNumber, " row data: ", tableArray[rowNumber]);
        // check every column in the row
        do {
            // console.log("checking column number", columnNumber);
            if (tableArray[rowNumber][columnNumber] == calledNumber) {
                tableArray[rowNumber][columnNumber] = 'XX'
                // if number found, immediately return new array
                return {
                    newTableArray: tableArray,
                    rowNumber: rowNumber,
                    columnNumber: columnNumber
                }
            } else {
                // otherwise, check the next number in the row
                columnNumber++;
            }
        } while (columnNumber < 5)

        // if not found in that row, reset column to zero and move to next row
        columnNumber = 0;
        rowNumber++;

    } while (rowNumber < 5)

    return false;

}

const testTable = [
    [ '14', '21', '17', '24', '4' ],
    [ '10', '16', '15', '9', '19' ],
    [ '18', '8', '23', '26', '20' ],
    [ '22', '11', '13', '6', '5' ],
    [ '2', '0', '12', '3', '7' ]
]

// iterate through called numbers
for (let a=0; a < calledNumsArray.length; a++) {
    const currentNumber = calledNumsArray[a];
    console.log("current called number equals", currentNumber);

    // now iterate through all tables in the array
    for (let d=0; d < fullTablesArray.length; d++) {
        let currentTable = fullTablesArray[d];

        // make sure it hasn't already won
        if (currentTable != 'already bingo') {
            const isNumberInTable = checkTableForNumber(currentTable, currentNumber);

            if (isNumberInTable != false) {
                // console.log("I found the number! here's the new array: ", isNumberInTable);
                // console.log("now checking for bingo...");
                const bingo = checkTableForBingo(isNumberInTable.newTableArray, isNumberInTable.rowNumber, isNumberInTable.columnNumber);
                if (bingo) {
                    console.log("Table Number ", d, " has bingo!!! Table details:", isNumberInTable.newTableArray)
                    // now iterate through every item within every item in the new array and add them together
                    let totalSum = 0;
                    for (let b=0; b<isNumberInTable.newTableArray.length; b++) {
                        isNumberInTable.newTableArray[b].forEach((item) => {
                            if (item != 'XX') {
                                const numItem = parseInt(item);
                                totalSum += numItem;
                            }
                        })
                    }
                    console.log("currentNumber: ", currentNumber, totalSum*currentNumber);
                    // I can't fully remove it because it fucks with the iteration over the list
                    // instead just label it and leave it in there
                    console.log("removing this table from rotation")
                    fullTablesArray[d] = "already bingo";
                } else {
                    console.log("sorry, no bingo yet")
                }
            }
        }
    }
}

// console.log(checkColumnForBingo(testFullArray, 4));
// console.log(checkForBingo(testRow));