#!/usr/bin/node

const request = require('request');
const writeFile = require('fs').writeFile;

const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    writeFile(file, body, err => {
      if (err) console.log(err);
    });
  }
});
