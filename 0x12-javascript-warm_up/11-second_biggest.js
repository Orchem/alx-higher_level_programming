#!/usr/bin/node
const len = process.argv.length;
if (len < 3) {
  console.log(0);
} else {
  const numArray = process.argv.slice(2);

  let firstBiggest = 0;
  let secondBiggest = 0;

  for (let count = 0; count < len; count++) {
    if (parseInt(numArray[count]) > firstBiggest) {
      secondBiggest = firstBiggest;
      firstBiggest = parseInt(numArray[count]);
    } else if (parseInt(numArray[count]) > secondBiggest) {
      secondBiggest = parseInt(numArray[count]);
    }
  }
  console.log(secondBiggest);
}
