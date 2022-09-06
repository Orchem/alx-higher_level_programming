#!/usr/bin/node
const variable = process.argv[2];
const num = parseInt(variable);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + variable);
}
