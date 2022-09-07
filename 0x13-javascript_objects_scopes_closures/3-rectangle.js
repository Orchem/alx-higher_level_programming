#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let side = '';
    for (let count = 0; count < this.width; count++) {
      side = side + 'X';
    }

    for (let count = 0; count < this.height; count++) {
      console.log(side);
    }
  }
}

module.exports = Rectangle;
