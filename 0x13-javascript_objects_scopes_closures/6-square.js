#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let b = '';
      for (let j = 0; j < this.width; j++) {
        b += c;
      }
      console.log(b);
    }
  }
}

module.exports = Square;
