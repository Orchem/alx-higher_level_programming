#!/usr/bin/node
const occurance = parseInt(process.argv[2]);

if (isNaN(occurance)) {
  console.log('Missing number of occurrences');
} else if (occurance > 0) {
  for (let count = 0; count < occurance; count++) {
    console.log('C is fun');
  }
}
