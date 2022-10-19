#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = '/18/';
let moviesCount = 0;

request(url, (error, response, body) => {
  const data = JSON.parse(body);
  if (error) {
    console.log(error);
    return;
  }

  for (const film of data.results) {
    for (const character of film.characters) {
      if (character.endsWith(id)) {
        moviesCount = moviesCount + 1;
      }
    }
  }
  console.log(moviesCount);
});
