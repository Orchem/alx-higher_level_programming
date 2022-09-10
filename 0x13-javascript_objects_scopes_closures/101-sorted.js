#!/usr/bin/node

const data = require('./101-data').dict;

const sortedData = {};
for (const key in data) {
  const newKey = data[key];
  if (newKey in sortedData) {
    sortedData[newKey].push(key);
  } else {
    sortedData[newKey] = [key];
  }
}

console.log(sortedData);
