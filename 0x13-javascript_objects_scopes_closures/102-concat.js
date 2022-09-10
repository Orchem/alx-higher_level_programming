#!/usr/bin/node

const fs = require('fs');

function concat (firstFile, secondFile, saveFile) {
  const content1 = fs.readFileSync(firstFile);
  const content2 = fs.readFileSync(secondFile);

  fs.writeFileSync(saveFile, (content1 + content2));
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

if (process.argv.length === 5) {
  concat(file1, file2, file3);
}
