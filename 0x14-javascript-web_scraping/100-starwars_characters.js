#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

let character;
const characters = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body).characters;
	data.sort();
  for (const characterUrl of data) {
    request(characterUrl, (error2, response2, body2) => {
      if (error2) {
        console.log(error2);
      }
      character = JSON.parse(body2);
      console.log(character.name);
      characters.push(character.name);
    });
  }

  for (const name of characters) {
    console.log(name);
  }
});
