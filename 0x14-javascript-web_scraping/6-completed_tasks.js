#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const completedTasks = {};

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  for (const todo of data) {
    if (todo.completed === true) {
      if (todo.userId in completedTasks) {
        completedTasks[todo.userId] = completedTasks[todo.userId] + 1;
      } else {
        completedTasks[todo.userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});
