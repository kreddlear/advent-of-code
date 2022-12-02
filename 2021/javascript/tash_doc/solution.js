// read file

const fs = require('fs');

// get it into an array that's possible to split
const data = fs.readFileSync('./input.txt', 'utf8');
const stringData = data.toString();
const stringArrayData = stringData.split('\n');
console.log(stringArrayData);

let newArrayOfData = [];

// iterate through rows
for (let i=0; i < stringArrayData.length; i++) {
    const columnArray = stringArrayData[i].split(',');

    // iterate through columns in row
    let strippedColumnArray = [];
    for (let j=0; j < columnArray.length; j++) {
        // strip out whitespace and commas
        if (columnArray[j] != '' && columnArray[j] != ' ') {
            strippedColumnArray.push(columnArray[j]);
        }
    }

    // create a new item that's stripped of unnecessary tags
    let newColumnObject = {
        ticketId: ' ',
        firstDate: ' ',
        secondDate: ' ',
        incident: ' ',
        severity: ' ',
        plan: ' ',
        team: ' ',
    };
    const teamArray = ['paid', 'onboarding-monthly', 'onboarding-annual', 'associate-cc']
    const planArray = ['free', 'starter', 'pro', 'professional', 'professional-plus', 'team', 'no-plan', 'hv-trial']
    for (let l=0; l < strippedColumnArray.length; l++) {
        // add the ticket ID
        if (l==0) {
            newColumnObject.ticketId = strippedColumnArray[l];
        }
        else if (l==1) {
            newColumnObject.firstDate = strippedColumnArray[l];
        }
        // if it's got a second date, include it, or set it as blank
        else if (l==2 && strippedColumnArray[l].includes('2022')) {
            newColumnObject.secondDate = strippedColumnArray[l];
        }
        // check if it's an incident tag
        else if (strippedColumnArray[l].includes('incident') && !strippedColumnArray[l].includes('sev')) {
            newColumnObject.incident = strippedColumnArray[l];
        }
        // check if it's severity
        else if (strippedColumnArray[l].includes('sev')) {
            newColumnObject.severity = strippedColumnArray[l];
        }
        // check if it's a plan tag
        else if (planArray.includes(strippedColumnArray[l])) {
            newColumnObject.plan = strippedColumnArray[l];
        }
        // check if it's a team tag
        else if (teamArray.includes(strippedColumnArray[l])) {
            newColumnObject.team = strippedColumnArray[l];
        }
    }

    // turn the object into an array
    // concat the strings together, separated by commas
    const strippedString = (Object.values(newColumnObject)).join(',');

    // push string to the array
    newArrayOfData.push(strippedString);
}

// concat array together with newlines
const fullresults = newArrayOfData.join('\n')

try {
    fs.writeFileSync('./results.txt', fullresults)
    //file written successfully
  } catch (err) {
    console.error(err)
  }