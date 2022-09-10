#!/usr/bin/node

exports.logMe = function (item) {
  this.logs = (this.logs || 0);
  console.log(`${this.logs}: ${item}`);
  this.logs++;
};
