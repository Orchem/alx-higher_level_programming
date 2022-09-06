#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let side = '';
  for (let length = 0; length < size; length++) {
    side = side + 'X';
  }
  for (let width = 0; width < size; width++) {
    console.log(side);
  }
}
