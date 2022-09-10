#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c = 'X') {
    let side = '';
    for (let count = 0; count < this.width; count++) {
      side = side + c;
    }
    for (let count = 0; count < this.height; count++) {
      console.log(side);
    }
  }
}

module.exports = Square;
