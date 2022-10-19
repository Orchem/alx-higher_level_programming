#!/usr/bin/node

const fs = require('fs');
const arg = process.argv.slice(2);

fs.writeFile(arg[0], arg[1], error => {
  if (error) console.log(error);
});
